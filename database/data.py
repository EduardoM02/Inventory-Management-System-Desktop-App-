from .models.movement import MovementType

categories_data = [
    {"name": "Electrónicos", "description": "Productos electrónicos y gadgets."},
    {"name": "Accesorios", "description": "Accesorios para computadoras y teléfonos."},
    {"name": "Oficina", "description": "Artículos para trabajo y oficina."},
]

products_data = [
    {
        "name": "Teclado Mecánico RGB",
        "category_id": 1,
        "description": "Teclado mecánico con switches rojos.",
        "stock": 25,
        "price": 1299.99,
    },
    {
        "name": "Mouse Inalámbrico",
        "category_id": 1,
        "description": "Mouse óptico inalámbrico con batería recargable.",
        "stock": 40,
        "price": 499.50,
    },
    {
        "name": "Base para Laptop",
        "category_id": 2,
        "description": "Base ergonómica ajustable para laptops.",
        "stock": 15,
        "price": 699.00,
    },
    {
        "name": "Calculadora Científica",
        "category_id": 3,
        "description": "Calculadora científica con pantalla LCD.",
        "stock": 10,
        "price": 299.00,
    }
]

movements_data = [
    {"product_id": 1, "type": MovementType.IN.value, "quantity": 10},
    {"product_id": 1, "type": MovementType.OUT.value, "quantity": 3},
    {"product_id": 2, "type": MovementType.IN.value, "quantity": 20},
    {"product_id": 3, "type": MovementType.OUT.value, "quantity": 2},
    {"product_id": 4, "type": MovementType.IN.value, "quantity": 5},
]

