# backend/agents/underwriting.py
from ..services.credit_api import mock_fetch_credit_score
from ..models.loan_schema import LoanApplication

class UnderwritingAgent:
    def start_next_phase(self, data) -> str:
        # Fetch mock credit score automatically using the collected PAN
        data.mock_credit_score = mock_fetch_credit_score(data.pan_number)
        
        return (f"Welcome to Underwriting. We've fetched your mock score ({data.mock_credit_score}). "
                f"Please provide your **mock Annual Income** (e.g., $75000) for final assessment.")

    def process(self, user_message: str, data: LoanApplication) -> tuple[str, str]:
        """Collects income and applies mock underwriting rules to decide."""
        
        if not data.annual_income:
            # Extract income (simple number extraction)
            import re
            match = re.search(r'\d[\d,\.]+', user_message)
            if match:
                data.annual_income = int(re.sub(r'[^\d]', '', match.group(0)))

        if not data.annual_income:
            return ("Please provide your mock Annual Income to complete the assessment.", "")

        # --- Mock Underwriting Logic ---
        score = data.mock_credit_score
        income = data.annual_income
        requested = data.requested_amount
        
        # Rule 1: Minimum Credit Score and Income
        if score < 650 or income < 40000:
            data.status = "Rejected"
            return ("Based on mock criteria (low score/income), application rejected.", "REJECTED")

        # Rule 2: Calculate Sanction Terms
        max_sanction_by_income = int(income * 4.5) # Max 4.5x income
        
        sanctioned_amount = min(requested, max_sanction_by_income)
        
        # Rule 3: Set interest rate based on mock score tiers
        if score >= 750:
            rate = 7.5
        elif score >= 650:
            rate = 9.5
        else: # Should be caught by Rule 1, but safe fallback
            rate = 12.0
            
        data.status = "Approved"
        data.sanctioned_amount = sanctioned_amount
        data.interest_rate = rate
        data.tenure_months = 60  # Fixed tenure for demo
        
        response = (f"**Decision Made.** Sanctioned ${sanctioned_amount:,} at {rate}% over 60 months.")
        return (response, "APPROVED") # Signal specific completion