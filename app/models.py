from pydantic import BaseModel
from typing import List

class Prompt(BaseModel):
    id: int
    prompt: str

class User(BaseModel):
    id: int
    name: str

class PromptRequest(BaseModel):
    prompt: str
    user_id: int

class LLMResponse(BaseModel):
    response: str
