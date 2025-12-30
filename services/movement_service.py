
from database.models.movement import Movement, MovementType
from database.repositories.movement_repository import MovementRepository
from database.schemas.movement_schema import MovementCreate, MovementUpdate


class MovementService:
    def __init__(self, repo: MovementRepository | None = None):
        self.repo = repo or MovementRepository()

    def search_movement(self, query: str) -> list[dict]:
        if not query or len(query.strip()) < 2:
            return []

        movements = self.repo.search(query)
        return self._to_dict_list(movements)

    def get_all_movements(self) -> list[dict]:
        movements = self.repo.get_all()
        return self._to_dict_list(movements)

    def get_movement_by_id(self, movement_id: int) -> Movement:
        movement = self.repo.get_by_id(movement_id)
        if not movement:
            raise ValueError("Movement not found")
        return movement

    def add_movement(self, data: MovementCreate) -> Movement:
        data = MovementCreate(**data)
        try:
            data['type'] = MovementType(data['type'])
        except ValueError:
            raise ValueError("Invalid movement type")

        return self.repo.add(data)

    def update_movement(self, movement_id: int, data: MovementUpdate) -> Movement:
        data = MovementUpdate(**data)

        if not any(data.values()):
            raise ValueError("No fields provided to update")

        if data['type'] is not None:
            try:
                data['type'] = MovementType(data['type'])
            except ValueError:
                raise ValueError("Invalid movement type")

        movement = self.repo.update(movement_id, data)

        if not movement:
            raise ValueError("Movement not found")

        return movement

    def delete_movement(self, movement_id: int) -> None:
        if not self.repo.delete(movement_id):
            raise ValueError("Movement not found")

    def _to_dict_list(self, movements: list[Movement]) -> list[dict]:
        return [
            {
                "id": m.id,
                "product_id": m.product.id,
                "product_name": m.product.name,
                "type": m.type.value,
                "quantity": m.quantity,
                "date": m.date,
                "note": m.note,
            }
            for m in movements
        ]
