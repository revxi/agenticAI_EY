# backend/main.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict
import uuid

# Import the Master Agent
from .agents.master import LoanOrchestrator

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

class ChatRequest(BaseModel):
    conversation_id: str
    message: str

class ChatResponse(BaseModel):
    response: str

# --- Endpoints ---

@app.post("/start", response_model=StartResponse)
async def start_new_session():
    """Initializes a new Loan Orchestrator and returns the first prompt."""
    session_id = str(uuid.uuid4())
    orchestrator = LoanOrchestrator()
    
    initial_response = orchestrator.start_conversation()
    
    active_sessions[session_id] = orchestrator
    
    return StartResponse(
        conversation_id=session_id,
        response=initial_response
    )

@app.post("/chat", response_model=ChatResponse)
async def handle_chat_message(request: ChatRequest):
    """Routes the user message to the appropriate agent via the Orchestrator."""
    session_id = request.conversation_id
    
    orchestrator = active_sessions.get(session_id)
    
    if not orchestrator:
        raise HTTPException(status_code=404, detail="Session not found or expired.")
    
    agent_response = orchestrator.process_message(request.message)
    
    # If the process is completed or rejected, you could optionally remove the session here
    # if orchestrator.current_state in [WorkflowState.COMPLETED, WorkflowState.REJECTED]:
    #     del active_sessions[session_id]

    return ChatResponse(response=agent_response)

@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "LoanFlow Backend"}

# To run the FastAPI server (often done via uvicorn in a real setup):
# uvicorn main:app --reload