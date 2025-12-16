"""Minimal Pydantic models for loan data used by agents.

These are intentionally small placeholders to allow development
and early integration tests. Expand with real fields later.
"""

from pydantic import BaseModel
from typing import Optional


class LoanApplication(BaseModel):
	requested_amount: Optional[int] = None
	purpose: Optional[str] = None
	applicant_name: Optional[str] = None
	status: str = "Pending"
	sanctioned_amount: Optional[int] = None


class LoanStatus(BaseModel):
	status: str = "Pending"
	notes: Optional[str] = None
