from fastapi import FastAPI, BackgroundTasks, HTTPException
from app.core.logger import logger
from app.services.ingestion import run_ingestion_pipeline

app = FastAPI(title="EYE Engine")

@app.get("/health")
def health():
    logger.info("Health check OK")
    return {"status": "healthy"}

@app.get("/test")
def test():
    logger.info("Test OK")
    return {"status": "tested"}

@app.post("/ingest")
async def trigger_ingestion(background_tasks: BackgroundTasks, force: bool = False):
    """
    Trigger the document ingestion pipeline in the background.
    """
    logger.info(f"Received ingestion request (force={force})")
    try:
        # Run ingestion in background so we don't block the response
        background_tasks.add_task(run_ingestion_pipeline, force_refresh=force)
        return {"message": "Ingestion started in background", "force_refresh": force}
    except Exception as e:
        logger.error(f"Failed to trigger ingestion: {e}")
        raise HTTPException(status_code=500, detail=str(e))