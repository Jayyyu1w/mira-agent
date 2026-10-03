from typing import TypedDict


class WebResult(TypedDict):
    content: str
    title: str
    url: str
    published_at: str | None
    source: str | None