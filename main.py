from fastapi import FastAPI
from app.core.logger import logger
from app.middlewares.request_id import RequestIdMiddleware

logger.info("Hello from main.py (top level)")
logger.info("Hello from main.py (top level - stdout)")

app = FastAPI()
app.add_middleware(RequestIdMiddleware)

@app.get("/health")
def health():
    logger.info("Health check called!")
    return {"status": "ok"}