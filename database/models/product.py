from datetime import datetime
from decimal import Decimal

from sqlalchemy import ForeignKey, Text, Integer, String, DateTime, func, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    stock: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    category: Mapped["Category"] = relationship(back_populates="products")
    movements: Mapped[list["Movement"]] = relationship(back_populates="product")

    def __repr__(self) -> str:
        return f'<Product(id={self.id}, name={self.name}, category_id={self.category_id}, description={self.description}, stock={self.stock}, price={self.price}, created_at={self.created_at})>'
