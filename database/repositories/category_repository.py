from typing import List

from database import SessionLocal
from database.models import Category
from database.schemas import CategoryCreate, CategoryUpdate


class CategoryRepository:
    def search(self, query: str) -> List[Category]:
        with SessionLocal() as session:
            return (
                session.query(Category)
                .filter(Category.name.ilike(f"%{query}%"))
                .all()
            )

    def exists_by_name(self, name: str) -> bool:
        with SessionLocal() as session:
            return (
                session.query(
                    session.query(Category)
                    .filter(Category.name.ilike(f"%{name}%"))
                    .exists()
                )
                .scalar()
            )

    def get_all(self) -> List[Category]:
        with SessionLocal() as session:
            return (
                session.query(Category)
                .all()
            )

    def get_by_id(self, category_id: int) -> Category | None:
        with SessionLocal() as session:
            return (
                session.query(Category)
                .filter(Category.id == category_id)
                .one_or_none()
            )

    def add(self, data: CategoryCreate) -> Category:
        with SessionLocal() as session:
            category = Category(**data)
            session.add(category)
            session.commit()
            session.refresh(category)
            return category

    def update(self, category_id: int, data: CategoryUpdate) -> Category | None:
        with SessionLocal() as session:
            category = session.query(Category).filter(Category.id == category_id).one_or_none()

            if not category:
                return None

            for key, value in data.items():
                setattr(category, key, value)

            session.commit()
            session.refresh(category)
            return category

    def delete(self, category_id: int) -> bool:
        with SessionLocal() as session:
            category = session.query(Category).filter(Category.id == category_id).one_or_none()
            if not category:
                return False

            session.delete(category)
            session.commit()
            return True