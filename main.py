import logging
from fastapi import FastAPI

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)

logger = logging.getLogger("eye")

app = FastAPI()

@app.get("/health")
def health():
    logger.info("Health check OK")
    return {"status": "healthy"}

@app.get("/test")
def test():
    logger.info("Test OK")
    return {"status": "tested"}