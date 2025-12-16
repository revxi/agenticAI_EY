# backend/agents/sanction.py
from ..services.pdf_generator import generate_sanction_letter
from ..models.loan_schema import LoanApplication

class DocumentAgent:
    def start_next_phase(self, data) -> str:
        # This phase is triggered automatically by the Master Agent upon 'APPROVED' signal
        return "Initiating final document production..."

    def process(self, user_message: str, data) -> tuple[str, bool]:
        # This agent should not receive messages, only be triggered by the Orchestrator
        return ("Document process failed: Received unexpected message.", False)

    def generate_sanction_letter(self, data: LoanApplication) -> str:
        """Triggers the service layer to create the PDF and returns the mock link."""
        
        pdf_link = generate_sanction_letter(data)
        data.pdf_link = pdf_link
        
        # Returns the link to the Master Agent for final presentation
        return pdf_link