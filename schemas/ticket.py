from pydantic import BaseModel


class TicketCreate(BaseModel):
    customer_id: int
    title: str
    description: str
    priority: str
    category: str


class TicketUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    priority: str | None = None
    category: str | None = None
    status: str | None = None


class TicketResponse(BaseModel):
    id: int
    customer_id: int
    title: str
    description: str
    priority: str
    category: str
    status: str
    assigned_agent: int | None

    class Config:
        from_attributes = True
