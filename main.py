from fastapi import FastAPI
from app.api import router as api_router
import uvicorn

app = FastAPI(title="Dummy LLM Vertex AI API")

app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
