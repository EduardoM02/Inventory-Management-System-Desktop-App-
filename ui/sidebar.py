from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton

class Sidebar(QWidget):
    def __init__(self):
        super().__init__()

        self.btn_categories = QPushButton("Categories")
        self.btn_products = QPushButton("Products")
        self.btn_movements = QPushButton("Movements")

        layout = QVBoxLayout()
        layout.addWidget(self.btn_categories)
        layout.addWidget(self.btn_products)
        layout.addWidget(self.btn_movements)
        layout.addStretch()

        self.setLayout(layout)
