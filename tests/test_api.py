import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from fastapi.testclient import TestClient
from main import app

def test_generate_text():
    client = TestClient(app)
    response = client.post("/api/generate", json={"prompt": "Test prompt", "user_id": 1})
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert "Test prompt" in data["response"]
