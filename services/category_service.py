from database.models.category import Category
from database.repositories.category_repository import CategoryRepository
from database.schemas.category_schema import CategoryCreate, CategoryUpdate


class CategoryService:
    def __init__(self, repo: CategoryRepository | None = None):
        self.repo = repo or CategoryRepository()

    def search_categories(self, query: str) -> list[dict]:
        if not query:
            return []

        categories = self.repo.search(query)
        return self._to_dict_list(categories)

    def get_all_categories(self) -> list[dict]:
        categories = self.repo.get_all()
        return self._to_dict_list(categories)

    def get_category_by_id(self, category_id: int) -> Category:
        category = self.repo.get_by_id(category_id)
        if not category:
            raise ValueError("Category not found")
        return category

    def add_category(self, data: dict) -> Category:
        data = CategoryCreate(**data)

        if self.repo.exists_by_name(data['name']):
            raise ValueError("Category name already exists")

        return self.repo.add(data)

    def update_category(self, category_id: int, data: dict) -> Category:
        data = CategoryUpdate(**data)

        if not data:
            raise ValueError("No fields provided to update")
        category = self.repo.update(category_id, data)

        if not category:
            raise ValueError("Category not found")
        return category

    def delete_category(self, category_id: int) -> None:
        deleted = self.repo.delete(category_id)
        if not deleted:
            raise ValueError("Category not found")

    def _to_dict_list(self, categories):
        return [
            {
                "id": c.id,
                "name": c.name,
                "description": c.description,
            }
            for c in categories
        ]