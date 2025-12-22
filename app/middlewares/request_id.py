import uuid
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.logger import logger

class RequestIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = request.headers.get("x-request-id", str(uuid.uuid4()))
        request.state.request_id = request_id

        # “bind” por request
        request_logger = logger.bind(
            request_id=request_id,
            method=request.method,
            path=request.url.path,
        )

        request_logger.info("request_start")
        try:
            response = await call_next(request)
            request_logger.bind(status_code=response.status_code).info("request_end")
            response.headers["x-request-id"] = request_id
            return response
        except Exception:
            request_logger.exception("request_failed")
            raise
