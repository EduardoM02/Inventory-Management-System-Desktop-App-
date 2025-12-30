from typing import List

from sqlalchemy import or_
from sqlalchemy.orm import joinedload
from database import SessionLocal
from database.models import Movement, Product
from database.schemas import MovementUpdate, MovementCreate

class MovementRepository:
    def search(self, query: str) -> list[Movement]:
        with SessionLocal() as session:
            return (
                session.query(Movement)
                .join(Movement.product)
                .options(joinedload(Movement.product))
                .filter(
                    or_(
                        Product.name.ilike(f"%{query}%"),
                        Movement.note.ilike(f"%{query}%"),
                    )
                )
                .all()
            )

    def get_all(self):
        with SessionLocal() as session:
            return (
                session.query(Movement)
                .options(joinedload(Movement.product))
                .all()
            )

    def get_by_id(self, movement_id: int) -> Movement | None:
        with SessionLocal() as session:
            return (
                session.query(Movement)
                .options(joinedload(Movement.product))
                .filter(Movement.id == movement_id)
                .one_or_none()
            )

    def add(self, data: MovementCreate) -> Movement | None:
        with SessionLocal() as session:
            movement = Movement(**data)
            session.add(movement)
            session.commit()
            session.refresh(movement)
            return movement

    def update(self, movement_id: int, data: MovementUpdate) -> Movement | None:
        with SessionLocal() as session:
            movement = session.query(Movement).filter(Movement.id == movement_id).one_or_none()

            if not movement:
                return None

            for key, value in data.items():
                setattr(movement, key, value)

            session.commit()
            session.refresh(movement)
            return movement

    def delete(self, movement_id: int) -> bool:
        with SessionLocal() as session:
            movement = session.query(Movement).filter(Movement.id == movement_id).one_or_none()

            if not movement:
                return False

            session.delete(movement)
            session.commit()
            return True
