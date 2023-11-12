from pydantic import BaseModel


class Ticket(BaseModel):
    title: str
    description: str
    category: str
    priority: int
    progress: int
    status: str
    active: bool
