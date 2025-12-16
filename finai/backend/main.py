session_state = {
    "stage": "Sales",
    "logs": []
}

# backend/main.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
# ... and you should also have pydantic for your models
from pydantic import BaseModel
from typing import Dict
import uuid

# Import the Master Agent and helper
from agents.master import LoanOrchestrator, master_agent
from services.crm_api import create_crm_lead

app = FastAPI(title="Agentic LoanFlow Backend")

# --- CORS Configuration ---
# IMPORTANT: This allows your frontend to talk to your backend on different ports
origins = [
    "http://127.0.0.1:8000",  # Your FastAPI server
    "http://localhost:8000",
    "http://127.0.0.1:5500",  # Common port for VS Code Live Server
    # Add the URL where you open index.html
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For simplicity in a demo, allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Session Management ---
# Store active Orchestrator instances keyed by a unique conversation ID
active_sessions: Dict[str, LoanOrchestrator] = {}

# --- Pydantic Models for Requests ---
class StartResponse(BaseModel):
    conversation_id: str
    response: str
    active_agent: str


class ChatResponse(BaseModel):
    response: str
    active_agent: str


# --- Endpoints ---

@app.post("/start", response_model=StartResponse)
async def start_new_session():
    """Initializes a new Loan Orchestrator and returns the first prompt."""
    session_id = str(uuid.uuid4())
    orchestrator = LoanOrchestrator()
    # Create a CRM lead for this session (minimal data for now)
    lead_id = create_crm_lead({"session_id": session_id})
    orchestrator.lead_id = lead_id

    initial_response = orchestrator.start_conversation()
    
    active_sessions[session_id] = orchestrator
    
    return StartResponse(
        conversation_id=session_id,
        response=initial_response,
        active_agent=orchestrator.get_active_agent()
    )


@app.post("/chat")
def chat(payload: dict):
    """Routes messages through the agent pipeline.

    Returns JSON with response, active_agent, and session info.
    """
    message = payload.get("message", "")

    # If a conversation_id is provided, route to the existing session-based orchestrator
    conv_id = payload.get("conversation_id") or payload.get("conversationId")
    if conv_id:
        orchestrator = active_sessions.get(conv_id)
        if not orchestrator:
            raise HTTPException(status_code=404, detail="Session not found or expired.")
        agent_response = orchestrator.process_message(message)
        return ChatResponse(
            response=agent_response,
            active_agent=orchestrator.get_active_agent()
        )

    # Stateless/simple mode: delegate to master_agent and provide both 'reply' and 'response'
    reply = master_agent(message)
    return {"reply": reply, "response": reply, "active_agent": "🟢 Sales Agent Active"}

@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "LoanFlow Backend"}

# To run the FastAPI server (often done via uvicorn in a real setup):
# uvicorn main:app --reload