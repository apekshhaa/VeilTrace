from datetime import datetime
from pydantic import BaseModel, Field
from uuid import uuid4
from typing import List


class Report(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))

    investigation_id: str

    summary: str

    risk_score: float

    findings: List[str] = []

    recommendations: List[str] = []

    generated_at: datetime = Field(default_factory=datetime.utcnow)