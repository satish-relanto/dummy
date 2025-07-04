# Dummy LLM Vertex AI FastAPI Backend

## Features
- FastAPI backend for LLM text generation using Google Vertex AI (simulated for demo)
- Dockerized for production deployment
- Uses environment variables for secrets
- Dummy data for prompts and users

## Setup

1. Copy `.env.example` to `.env` and fill in your Google API key and project info.
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run locally:
   ```sh
   uvicorn main:app --reload
   ```
4. Build and run with Docker:
   ```sh
   docker build -t dummy-llm-api .
   docker run --env-file .env -p 8080:8080 dummy-llm-api
   ```

## API Usage
- POST `/api/generate` with JSON body:
  ```json
  { "prompt": "Your prompt here", "user_id": 1 }
  ```
- Response:
  ```json
  { "response": "[VertexAI simulated response] Your prompt here" }
  ```

## Testing
- Run tests with pytest:
  ```sh
  pytest
  ```
