from pydantic import BaseModel

class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    question: str
    company: str
    year: int
    history: list | None = None


class ChatResponse(BaseModel):

    answer: str