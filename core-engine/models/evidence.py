from datetime import datetime
from typing import Any, Dict
from uuid import uuid4

from pydantic import BaseModel, Field


class Evidence(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))

    
    investigation_id: str | None = None

    type: str
    value: str

    severity: str
    confidence: float = 1.0

    source: str

    timestamp: datetime = Field(default_factory=datetime.utcnow)

    metadata: Dict[str, Any] = Field(default_factory=dict)