from PySide6.QtWidgets import QMainWindow, QStackedWidget, QWidget, QHBoxLayout

from services import CategoryService, MovementService, ProductService
from ui.category import CategoryView, CategoryController
from ui.movement import MovementView, MovementController
from ui.product import ProductView, ProductController
from ui.sidebar import Sidebar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Inventory System")
        self.resize(1100, 700)

        self.sidebar = Sidebar()
        self.stack = QStackedWidget()

        self.category_view = CategoryView()
        self.product_view = ProductView()
        self.movement_view = MovementView()

        self.stack.addWidget(self.category_view)
        self.stack.addWidget(self.product_view)
        self.stack.addWidget(self.movement_view)

        container = QWidget()
        layout = QHBoxLayout(container)
        layout.addWidget(self.sidebar)
        layout.addWidget(self.stack)

        self.setCentralWidget(container)

        self._setup_controllers()
        self._connect_sidebar()

    def _setup_controllers(self):
        category_service = CategoryService()
        product_service = ProductService()
        movement_service = MovementService()

        self.category_controller = CategoryController(
            view=self.category_view,
            service=category_service,
        )

        self.product_controller = ProductController(
            view=self.product_view,
            product_service=product_service,
            category_service=category_service
        )

        self.movement_controller = MovementController(
            view=self.movement_view,
            movement_service=movement_service,
            product_service=product_service,
        )

    def _connect_sidebar(self):
        self.sidebar.btn_categories.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.category_view)
        )

        self.sidebar.btn_products.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.product_view)
        )

        self.sidebar.btn_movements.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.movement_view)
        )

