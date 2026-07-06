from pydantic import BaseModel, EmailStr, Field


class CustomerCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str = Field(pattern=r"^[6-9]\d{9}$")
    address: str


class CustomerResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str
    address: str

    class Config:
        from_attributes = True
