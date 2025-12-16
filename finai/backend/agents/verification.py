# backend/agents/verification.py
from ..services.credit_api import mock_kyc_verification
from ..models.loan_schema import LoanApplication

class KYCAgent:
    def start_next_phase(self, data) -> str:
        return "Welcome to the Verification Stage. To proceed with your application, please provide your **mock PAN Number** and **mock Aadhaar Number** (e.g., PAN: ABCDE1234F, Aadhaar: 123456789012)."

    def process(self, user_message: str, data: LoanApplication) -> tuple[str, bool]:
        """Collects and attempts to verify mock PAN and Aadhaar."""
        
        # Simple extraction logic for demo
        import re
        pan_match = re.search(r'PAN:\s*([A-Z0-9]+)', user_message, re.IGNORECASE)
        aadhaar_match = re.search(r'Aadhaar:\s*(\d+)', user_message, re.IGNORECASE)

        if pan_match:
            data.pan_number = pan_match.group(1).upper()
        if aadhaar_match:
            data.aadhaar_number = aadhaar_match.group(1)

        # Attempt verification using the mock service
        if data.pan_number and data.aadhaar_number:
            is_verified = mock_kyc_verification(data.pan_number, data.aadhaar_number)
            data.is_kyc_verified = is_verified

            if is_verified:
                response = "**Identity Verified** (Mock Success). We can now move on to risk assessment."
                return (response, True) # Signal completion
            else:
                return ("Verification failed. Please re-enter both your mock PAN and Aadhaar numbers carefully.", False)
        
        return ("Please provide both your mock PAN and Aadhaar numbers to continue verification.", False)