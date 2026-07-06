from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Text

from sqlalchemy.orm import relationship

from database import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)

    description = Column(Text)

    priority = Column(String)

    category = Column(String)

    status = Column(String, default="Open")

    customer_id = Column(
        Integer,
        ForeignKey("customers.id")
    )

    assigned_agent = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True
    )

    customer = relationship(
        "Customer",
        back_populates="tickets"
    )

    agent = relationship("User")
