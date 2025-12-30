from datetime import datetime
from enum import Enum as PyEnum
from sqlalchemy import Enum as SAEnum
from sqlalchemy import ForeignKey, Integer, DateTime, func, String
from sqlalchemy.orm import Mapped, relationship, mapped_column
from database import Base

class MovementType(str, PyEnum):
    IN = 'in'
    OUT = 'out'


class Movement(Base):
    __tablename__ = "movements"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'), nullable=False)
    type: Mapped[MovementType] = mapped_column(SAEnum(MovementType, name="movement_type", native_enum=True, values_callable=lambda enums: [e.value for e in enums]), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    date: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    note: Mapped[str] = mapped_column(String(255), nullable=True)

    product: Mapped["Product"] = relationship(back_populates="movements")

    def __repr__(self) -> str:
        return f'Movement(id={self.id}, product_id={self.product_id}, type={self.type}, quantity={self.quantity}, date={self.date}, note={self.note})'
