import json
import logging
import os
import sys
from datetime import datetime, timezone
from typing import Any, Dict

from loguru import logger


def _env_bool(name: str, default: bool = False) -> bool:
    v = os.getenv(name)
    if v is None:
        return default
    return v.strip().lower() in {"1", "true", "yes", "y", "on"}


def _level() -> str:
    return os.getenv("LOG_LEVEL", "INFO").upper()


def _is_json() -> bool:
    return os.getenv("LOG_FORMAT", "pretty").lower() == "json"


def _service_name() -> str:
    return os.getenv("SERVICE_NAME", "eye-engine")


def _json_serializer(record: Dict[str, Any]) -> str:
    # JSON “industrial”: estável para parsing (Loki/ELK), inclui tracebacks.
    payload = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "level": record["level"].name,
        "message": record["message"],
        "logger": record["name"],
        "module": record["module"],
        "function": record["function"],
        "line": record["line"],
        "process": record["process"].id,
        "thread": record["thread"].id,
        "service": _service_name(),
        "extra": record["extra"],
    }
    if record["exception"]:
        payload["exception"] = {
            "type": str(record["exception"].type),
            "value": str(record["exception"].value),
            "traceback": record["exception"].traceback,
        }
    return json.dumps(payload, ensure_ascii=False)


class InterceptHandler(logging.Handler):
    """Redireciona logs do `logging` padrão (uvicorn/fastapi/libs) para Loguru."""

    def emit(self, record: logging.LogRecord) -> None:
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = logging.currentframe(), 2
        while frame and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(
            depth=depth,
            exception=record.exc_info,
        ).log(level, record.getMessage())


def configure_logger() -> None:
    logger.remove()

    # DEV friendliness
    dev_mode = _env_bool("DEV_MODE", default=False)
    backtrace = _env_bool("LOG_BACKTRACE", default=dev_mode)
    diagnose = _env_bool("LOG_DIAGNOSE", default=dev_mode)

    # 1) stdout sink (docker logs)
    if _is_json():
        logger.add(
            sys.stdout,
            level=_level(),
            serialize=False,  # usamos format custom para controle total
            format=_json_serializer,
            enqueue=True,
            backtrace=backtrace,
            diagnose=diagnose,
        )
    else:
        logger.add(
            sys.stdout,
            level=_level(),
            colorize=True,
            enqueue=True,
            backtrace=backtrace,
            diagnose=diagnose,
            format=(
                "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
                "<level>{level: <8}</level> | "
                "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
                "<level>{message}</level> | {extra}"
            ),
        )

    # 2) file sink (persistência + auditoria)
    log_dir = os.getenv("LOG_DIR", "logs")
    os.makedirs(log_dir, exist_ok=True)

    log_path = os.path.join(log_dir, os.getenv("LOG_FILE", "app.log"))
    logger.add(
        log_path,
        level=_level(),
        rotation=os.getenv("LOG_ROTATION", "50 MB"),
        retention=os.getenv("LOG_RETENTION", "14 days"),
        compression=os.getenv("LOG_COMPRESSION", "zip"),
        enqueue=True,
        backtrace=backtrace,
        diagnose=diagnose,
        format=_json_serializer if _is_json() else "{time} | {level} | {message} | {extra}",
    )

    # Intercept: tudo que for logging padrão vai pra Loguru
    logging.root.handlers = [InterceptHandler()]
    logging.root.setLevel(_level())

    for noisy in ("uvicorn", "uvicorn.error", "uvicorn.access", "fastapi"):
        logging.getLogger(noisy).handlers = [InterceptHandler()]
        logging.getLogger(noisy).propagate = False


# Configure no import (captura top-level bootstrap)
configure_logger()
