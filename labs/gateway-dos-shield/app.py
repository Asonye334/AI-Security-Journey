from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Mock LLM Gateway Target")

class PromptRequest(BaseModel):
    prompt: str

@app.get("/health")
def health_check():
    return {"status": "online", "secured": True}

@app.post("/v1/chat")
def mock_chat(payload: PromptRequest):
    if not payload.prompt:
        raise HTTPException(status_code=400, detail="Prompt payload cannot be empty.")
    
    return {
        "model": "mock-defense-llama-v1",
        "choices": [
            {
                "message": {
                    "role": "assistant",
                    "content": f"Acknowledged. Processing prompt: '{payload.prompt[:30]}...' within secure enclave."
                }
            }
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
