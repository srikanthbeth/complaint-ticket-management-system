from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship

from database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    email = Column(String, unique=True)

    phone = Column(String)

    address = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User")

    tickets = relationship(
        "Ticket",
        back_populates="customer",
        cascade="all,delete"
    )
