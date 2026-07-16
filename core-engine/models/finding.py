from pydantic import BaseModel, Field
from uuid import uuid4
from typing import List
class Finding(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))

    investigation_id: str
    title: str
    description: str
    severity: str
    confidence: float
    evidence_ids: List[str] = []