from decimal import Decimal

from PySide6.QtWidgets import QDialog, QLineEdit, QTextEdit, QComboBox, QPushButton, QFormLayout, QHBoxLayout, \
    QVBoxLayout, QMessageBox


class ProductForm(QDialog):
    def __init__(self, parent=None, categories=None, product=None):
        super().__init__(parent)

        self.product = product
        self.categories = categories or []
        self.is_edit = product is not None

        self.setWindowTitle("Edit Product" if self.is_edit else "New Product")
        self.setModal(True)

        # Fields
        self.name = QLineEdit()
        self.description = QTextEdit()
        self.category = QComboBox()
        self.stock = QLineEdit()
        self.price = QLineEdit()

        # UI config
        self.stock.setPlaceholderText("0")
        self.price.setPlaceholderText("0.00")

        self.load_categories()

        if self.is_edit:
            self.load_data()

        self.build_ui()

    def build_ui(self):
        btn_save = QPushButton("Save")
        btn_cancel = QPushButton("Cancel")

        btn_save.setDefault(True)

        btn_save.clicked.connect(self.on_save)
        btn_cancel.clicked.connect(self.reject)

        form = QFormLayout()
        form.addRow("Name:", self.name)
        form.addRow("Description:", self.description)
        form.addRow("Category:", self.category)
        form.addRow("Stock:", self.stock)
        form.addRow("Price:", self.price)

        buttons = QHBoxLayout()
        buttons.addStretch()
        buttons.addWidget(btn_save)
        buttons.addWidget(btn_cancel)

        main = QVBoxLayout()
        main.addLayout(form)
        main.addLayout(buttons)

        self.setLayout(main)

    def load_categories(self):
        self.category.clear()

        for category in self.categories:
            self.category.addItem(category['name'], category['id'])

    def load_data(self):
        self.name.setText(self.product.name)
        self.description.setText(self.product.description or "")
        self.stock.setText(str(self.product.stock))
        self.price.setText(str(self.product.price))

        index = self.category.findData(self.product.category_id)
        if index >= 0:
            self.category.setCurrentIndex(index)

    def on_save(self):
        if not self.name.text().strip():
            QMessageBox.warning(self, "Warning", "Name is required")
            return

        if self.category.currentIndex() < 0:
            QMessageBox.warning(self, "Warning", "Select a category")
            return

        try:
            int(self.stock.text())
            Decimal(self.price.text())
        except ValueError:
            QMessageBox.warning(self, "Warning", "Invalid stock or price")
            return

        self.accept()

    def get_data(self):
        return {
            "name": self.name.text().strip(),
            "description": self.description.toPlainText().strip(),
            "category_id": self.category.currentData(),
            "stock": int(self.stock.text()),
            "price": Decimal(self.price.text()),
        }
