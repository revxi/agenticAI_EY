# backend/services/credit_api.py
import random
from typing import Optional

def mock_kyc_verification(pan: str, aadhaar: str) -> bool:
    """Simulates verifying identity documents against a database."""
    # Mock Logic: Simple check that both mock IDs are provided and non-empty.
    if pan and aadhaar:
        print(f"[SERVICE] Mock KYC check successful for {pan}.")
        return True
    print("[SERVICE] Mock KYC check failed: missing data.")
    return False

def mock_fetch_credit_score(pan: str) -> Optional[int]:
    """Simulates fetching a credit score based on ID."""
    if pan:
        # Returns a score between 600 and 850 (random for the demo)
        score = random.randint(600, 850)
        print(f"[SERVICE] Mock Credit Score fetched: {score}.")
        return score
    return None