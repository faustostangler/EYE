
import sys
import os

# Add current directory to sys.path to ensure we can import app modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.services.ingestion import run_ingestion_pipeline

if __name__ == "__main__":
    # You can parse arguments here if needed
    run_ingestion_pipeline(force_refresh=True)
