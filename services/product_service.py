from database.models.product import Product
from database.repositories.product_repository import ProductRepository
from database.schemas.product_schema import ProductCreate, ProductUpdate


class ProductService:
    def __init__(self, repo: ProductRepository | None = None):
        self.repo = repo or ProductRepository()

    def search_product(self, query: str) -> list[dict]:
        if not query or len(query) < 2:
            return []

        products = self.repo.search(query)
        return self._to_dict_list(products)

    def get_all_products(self) -> list[dict]:
        products = self.repo.get_all()
        return self._to_dict_list(products)

    def get_product_by_id(self, product_id: int) -> Product:
        product = self.repo.get_by_id(product_id)
        if not product:
            raise ValueError("Product not found")
        return product

    def add_product(self, data: dict) -> Product:
        data = ProductCreate(**data)
        if not any(data.values()):
            raise ValueError("No fields provided")
        if self.repo.exists_by_name(data['name']):
            raise ValueError("Product name already exists")

        return self.repo.add(data)

    def update_product(self, product_id: int, data: ProductUpdate) -> Product:
        data = ProductUpdate(**data)

        if not any(data.values()):
            raise ValueError("No fields provided to update")

        product = self.repo.update(product_id, data)
        if not product:
            raise ValueError("Product not found")
        return product

    def delete_product(self, product_id: int) -> None:
        if self.repo.has_movements(product_id):
            raise ValueError(
                "The product cannot be deleted because it has associated movements"
            )

        if not self.repo.delete(product_id):
            raise ValueError("Producto not found")

    def _to_dict_list(self, products):
        return [
            {
                "id": p.id,
                "name": p.name,
                "category_id": p.category.id,
                "category_name": p.category.name,
                "price": p.price,
                "stock": p.stock,
                "description": p.description,
            }
            for p in products
        ]
