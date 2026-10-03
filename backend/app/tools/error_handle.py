from typing import TypedDict


class ToolError(TypedDict):
    type: str
    message: str


class ToolResult(TypedDict):
    success: bool
    data: object
    error: ToolError | None
    metadata: dict