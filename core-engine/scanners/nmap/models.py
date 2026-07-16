from pydantic import BaseModel, Field
from typing import Any, Dict, List
from datetime import datetime


class Finding(BaseModel):
    id: str
    type: str
    value: str
    severity: str
    confidence: float
    source: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class ScanResult(BaseModel):
    module: str
    status: str
    findings: List[Finding] = Field(default_factory=list)
