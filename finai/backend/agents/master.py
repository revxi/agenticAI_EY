"""Loan Orchestrator that routes through Sales → KYC → Underwriting → Sanction agents.

This module contains the `LoanOrchestrator` class that manages the conversation
state machine and delegates to specialized agents for each pipeline stage.
"""

from typing import Optional
import re

# CRM update helper
from services.crm_api import update_lead_status

# Import specialized agents
from agents.sales import HumanizerAgent
from agents.verification import KYCAgent
from agents.underwriting import UnderwritingAgent
from agents.sanction import DocumentAgent
from models.loan_schema import LoanApplication


class LoanOrchestrator:
    """Orchestrator that routes through Sales → KYC → Underwriting → Sanction agents."""

    AGENT_STAGES = ["SALES", "KYC", "UNDERWRITING", "SANCTION", "COMPLETED"]

    def __init__(self) -> None:
        self.current_stage: str = "SALES"  # Track which agent is active
        self.last_message: Optional[str] = None
        self.lead_id: Optional[str] = None
        
        # Loan application data shared across all agents
        self.application = LoanApplication()
        
        # Initialize agents
        self.sales_agent = HumanizerAgent()
        self.kyc_agent = KYCAgent()
        self.underwriting_agent = UnderwritingAgent()
        self.sanction_agent = DocumentAgent()

    def get_active_agent(self) -> str:
        """Return a displayable emoji + agent name."""
        agents = {
            "SALES": "🟢 Sales Agent Active",
            "KYC": "🟡 KYC Agent Verifying",
            "UNDERWRITING": "🔵 Underwriting Agent Evaluating",
            "SANCTION": "🟣 Sanction Agent Generating Letter",
            "COMPLETED": "✅ Application Complete",
        }
        return agents.get(self.current_stage, "Unknown")

    def start_conversation(self) -> str:
        """Initialize the conversation with the Sales agent."""
        self.current_stage = "SALES"
        return self.sales_agent.initial_prompt()

    def process_message(self, message: str) -> str:
        self.last_message = message
        
        # Route to the appropriate agent based on current stage
        if self.current_stage == "SALES":
            return self._handle_sales(message)
        elif self.current_stage == "KYC":
            return self._handle_kyc(message)
        elif self.current_stage == "UNDERWRITING":
            return self._handle_underwriting(message)
        elif self.current_stage == "SANCTION":
            return self._handle_sanction(message)
        else:
            return "Your application has been completed. Thank you!"

    def _handle_sales(self, message: str) -> str:
        """Sales agent collects loan purpose, amount, and employment."""
        response, is_complete = self.sales_agent.process(message, self.application)
        
        if is_complete:
            self.current_stage = "KYC"
            # Add KYC prompt to response
            kyc_prompt = self.kyc_agent.start_next_phase(self.application)
            return f"{response}\n\n{kyc_prompt}"
        
        return response

    def _handle_kyc(self, message: str) -> str:
        """KYC agent collects PAN and Aadhaar."""
        response, is_complete = self.kyc_agent.process(message, self.application)
        
        if is_complete:
            self.current_stage = "UNDERWRITING"
            underwriting_prompt = self.underwriting_agent.start_next_phase(self.application)
            return f"{response}\n\n{underwriting_prompt}"
        
        return response

    def _handle_underwriting(self, message: str) -> str:
        """Underwriting agent makes approval decision."""
        response, decision = self.underwriting_agent.process(message, self.application)
        
        if decision == "APPROVED":
            self.current_stage = "SANCTION"
            # Auto-generate sanction letter
            pdf_link = self.sanction_agent.generate_sanction_letter(self.application)
            
            # Update CRM
            if self.lead_id:
                update_lead_status(self.lead_id, "Approved")
            
            final_msg = f"\n\nYour sanction letter has been generated: {pdf_link}"
            self.current_stage = "COMPLETED"
            return f"{response}{final_msg}"
        
        elif decision == "REJECTED":
            if self.lead_id:
                update_lead_status(self.lead_id, "Rejected")
            self.current_stage = "COMPLETED"
        
        return response

    def _handle_sanction(self, message: str) -> str:
        """Sanction phase is auto-triggered; no user input expected."""
        self.current_stage = "COMPLETED"
        return "Your application process is complete."


def master_agent(message: str) -> str:
    """Stateless wrapper for simple demos."""
    orchestrator = LoanOrchestrator()
    if not (message or "").strip():
        return orchestrator.start_conversation()
    return orchestrator.process_message(message)
