from database import SessionLocal
from .data import movements_data
from .repositories import MovementRepository

movement_repo = MovementRepository()

for data in movements_data:
    print("DEBUG movement data:", data)
    t = data.get("type")
    print("  -> type repr:", repr(t))
    print("  -> type class:", type(t))
    print("  -> has .value?:", getattr(t, "value", None))
    movement_repo.add(data)
