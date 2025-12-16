# backend/agents/sales.py

class HumanizerAgent:
    def initial_prompt(self) -> str:
        return "Hello! I'm your loan assistant. To start, what is the **purpose** of the loan you need, and the **approximate amount** you are looking for?"

    def start_next_phase(self, data) -> str:
        # Should not be needed if flow is linear, but included for completeness
        return "Let's continue discussing your loan requirements."
        
    def process(self, user_message: str, data) -> tuple[str, bool]:
        """Collects purpose, amount, and employment. Advances to KYC when enough data is gathered."""
        
        # Simple keyword extraction for demo
        message_lower = user_message.lower()
        
        if not data.requested_amount:
            # Look for numbers (basic assumption)
            import re
            match = re.search(r'\d[\d,\.]+', message_lower)
            if match:
                # Mock extraction, converting string to integer
                data.requested_amount = int(re.sub(r'[^\d]', '', match.group(0)))
                
        if "car" in message_lower or "vehicle" in message_lower:
            data.loan_purpose = "Auto Loan"
        elif "home" in message_lower or "house" in message_lower:
            data.loan_purpose = "Mortgage Inquiry"
        else:
            data.loan_purpose = "Personal Loan"
            
        if not data.employment_status:
            if "employed" in message_lower or "job" in message_lower:
                data.employment_status = "Employed"
            elif "business" in message_lower or "self-employed" in message_lower:
                data.employment_status = "Self-Employed"
            elif "retired" in message_lower:
                data.employment_status = "Retired"

        # Check for completion criteria
        if data.requested_amount and data.loan_purpose and data.employment_status:
            response = (
                f"Thank you, {data.employment_status} applicant. We have noted you require "
                f"a **{data.loan_purpose}** for **${data.requested_amount:,}**. "
                f"We can now move to the official verification stage."
            )
            return (response, True) # Signal completion
        
        return ("Got it. To complete your application, can you also specify your **employment status** and the **exact amount** needed?", False)