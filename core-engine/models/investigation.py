# from datetime import datetime
# from pydantic import BaseModel, Field
# from uuid import uuid4


# class Investigation(BaseModel):
#     id: str = Field(default_factory=lambda: str(uuid4()))
#     name: str
#     target: str
#     status: str = "PENDING"
#     risk_score: float = 0.0
#     created_at: datetime = Field(default_factory=datetime.utcnow)
#     updated_at: datetime = Field(default_factory=datetime.utcnow)
from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, Field


class Investigation(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))

    name: str

    target: str

    status: str = "PENDING"

    created_at: datetime = Field(default_factory=datetime.utcnow)

    updated_at: datetime = Field(default_factory=datetime.utcnow)

    risk_score: float = 0.0