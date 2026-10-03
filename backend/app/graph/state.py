from typing import TypedDict

from langchain_core.messages import BaseMessage

from app.schemas.memory import Memory, MemoryUpdateResult
from app.schemas.retrieval import RetrievedDocument
from app.schemas.routing import Intent
from app.schemas.validation import ValidationResult
from app.schemas.web import WebResult


class state(TypedDict):
    # Runtime / conversation
    thread_id: str
    messages: list[BaseMessage]

    # Query
    user_query: str
    normalized_query: str

    # Context
    conversation_summary: str | None
    memory_context: list[Memory]

    # Workflow
    intent: Intent

    # Evidence
    retrieved_docs: list[RetrievedDocument] | None
    web_results: list[WebResult] | None

    # Validation
    validation_result: ValidationResult | None
    validation_reason: str | None

    # Memory
    memory_update_result: MemoryUpdateResult | None