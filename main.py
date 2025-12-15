from fastapi import FastAPI
from agents.master import master_agent

app = FastAPI()

@app.post("/chat")
def chat(payload: dict):
    user_message = payload["message"]
    response = master_agent(user_message)
    return {"reply": response}

