from fastapi import APIRouter, HTTPException
from .models import PromptRequest, LLMResponse
from .vertex_ai_client import VertexAIClient

router = APIRouter()
vertex_client = VertexAIClient()

@router.post("/generate", response_model=LLMResponse)
def generate_text(request: PromptRequest):
    if not request.prompt:
        raise HTTPException(status_code=400, detail="Prompt is required.")
    response = vertex_client.predict(request.prompt)
    return LLMResponse(response=response)
