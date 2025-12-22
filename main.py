from fastapi import FastAPI
import sys

print("Hello from main.py (top level)", file=sys.stderr)
print("Hello from main.py (top level - stdout)", file=sys.stdout)

app = FastAPI()

@app.get("/health")
def health():
    print("Health check called!", file=sys.stderr)
    return {"status": "ok"}