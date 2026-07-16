from typing import List
from uuid import uuid4

from pydantic import BaseModel, Field


class Finding(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))

    investigation_id: str

    title: str

    description: str

    severity: str

    confidence: float

    evidence_ids: List[str] = Field(default_factory=list)