# from datetime import datetime
# from pydantic import BaseModel, Field
# from uuid import uuid4


# class Task(BaseModel):
#     id: str = Field(default_factory=lambda: str(uuid4()))
#     investigation_id: str
#     module: str
#     priority: str = "MEDIUM"
#     status: str = "PENDING"
#     created_at: datetime = Field(default_factory=datetime.utcnow)
#     completed_at: datetime | None = None
from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, Field


class Task(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))

    investigation_id: str

    module: str

    status: str = "PENDING"

    priority: str = "MEDIUM"

    created_at: datetime = Field(default_factory=datetime.utcnow)

    completed_at: datetime | None = None