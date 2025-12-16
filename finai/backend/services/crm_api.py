"""Minimal CRM API stubs for development.

Provides simple functions to create and update CRM leads used by agents.
"""

import uuid
from typing import Dict, Any


def create_crm_lead(application: Dict[str, Any]) -> str:
    """Create a mock CRM lead and return its ID."""
    lead_id = f"LEAD-{uuid.uuid4().hex[:8]}"
    print(f"[CRM] Created lead {lead_id} for applicant={application.get('applicant_name')}")
    return lead_id


def update_lead_status(lead_id: str, status: str) -> bool:
    """Mock updating a lead's status in the CRM."""
    print(f"[CRM] Updated lead {lead_id} status -> {status}")
    return True
