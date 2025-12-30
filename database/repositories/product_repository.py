from typing import List
from sqlalchemy.orm import joinedload
from database import SessionLocal
from database.models import Product, Movement
from database.schemas import ProductCreate, ProductUpdate


class ProductRepository:
    def search(self, query: str):
        with SessionLocal() as session:
            return (
                session.query(Product)
                .options(joinedload(Product.category))
                .filter(Product.name.ilike(f"%{query}%"))
                .all()
            )

    def exists_by_name(self, name: str) -> bool:
        with SessionLocal() as session:
            return (
                session.query(
                    session.query(Product)
                    .filter(Product.name.ilike(f"%{name}%"))
                    .exists()
                )
                .scalar()
            )

    def get_all(self):
        with SessionLocal() as session:
            return (
                session.query(Product)
                .options(joinedload(Product.category))
                .all()
            )

    def get_by_id(self, product_id: int) -> Product | None:
        with SessionLocal() as session:
            return (
                session.query(Product)
                .options(joinedload(Product.category))
                .filter(Product.id == product_id)
                .one_or_none()
            )

    def add(self, data: ProductCreate) -> Product | None:
        with SessionLocal() as session:
            product = Product(**data)
            session.add(product)
            session.commit()
            session.refresh(product)
            return product

    def update(self, product_id: int, data: ProductUpdate) -> Product | None:
        with SessionLocal() as session:
            product = session.query(Product).filter(Product.id == product_id).one_or_none()

            if not product:
                return None

            for key, value in data.items():
                setattr(product, key, value)

            session.commit()
            session.refresh(product)
            return product

    def delete(self, product_id: int) -> bool:
        with SessionLocal() as session:
            product = session.query(Product).filter(Product.id == product_id).one_or_none()

            if not product:
                return False

            session.delete(product)
            session.commit()
            return True

    def has_movements(self, product_id: int) -> bool:
        with SessionLocal() as session:
            return (
                session.query(Movement)
                .filter(Movement.product_id == product_id)
                .first() is not None
            )