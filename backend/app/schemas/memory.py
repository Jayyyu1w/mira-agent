from datetime import datetime
from typing import Literal, TypedDict


class Memory(TypedDict):
    id: str
    content: str
    created_at: datetime
    updated_at: datetime


class MemoryUpdateResult(TypedDict):
    operation: Literal["CREATE", "UPDATE", "NOOP"]
    success: bool