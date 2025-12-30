from PySide6.QtWidgets import QDialog, QComboBox, QRadioButton, QLineEdit, QTextEdit, QPushButton, QFormLayout, \
    QHBoxLayout, QWidget, QVBoxLayout, QMessageBox


class MovementForm(QDialog):
    def __init__(self, parent=None, products=None, movement=None):
        super().__init__(parent)

        self.movement = movement
        self.products = products or []
        self.is_edit = movement is not None

        self.setWindowTitle("Edit Movement" if self.is_edit else "New Movement")
        self.setModal(True)

        self.product = QComboBox()
        self.rb_in = QRadioButton("In")
        self.rb_out = QRadioButton("Out")
        self.quantity = QLineEdit()
        self.note = QTextEdit()

        self.quantity.setPlaceholderText("0")
        self.rb_in.setChecked(True)

        self.load_products()

        if self.is_edit:
            self.load_data()

        self.build_ui()

    def build_ui(self):
        btn_save = QPushButton("Save")
        btn_cancel = QPushButton("Cancel")

        btn_save.setDefault(True)

        btn_save.clicked.connect(self.on_save)
        btn_cancel.clicked.connect(self.reject)

        type_layout = QHBoxLayout()
        type_layout.addWidget(self.rb_in)
        type_layout.addWidget(self.rb_out)

        type_widget = QWidget()
        type_widget.setLayout(type_layout)

        form = QFormLayout()
        form.addRow("Product", self.product)
        form.addRow("Quantity", self.quantity)
        form.addRow("Type", type_widget)
        form.addRow("Note", self.note)

        buttons = QHBoxLayout()
        buttons.addStretch()
        buttons.addWidget(btn_save)
        buttons.addWidget(btn_cancel)

        main = QVBoxLayout()
        main.addLayout(form)
        main.addLayout(buttons)

        self.setLayout(main)

    def load_products(self):
        self.product.clear()

        for product in self.products:
            self.product.addItem(product['name'], product['id'])

    def load_data(self):
        self.quantity.setText(str(self.movement.quantity))
        self.note.setText(self.movement.note or "")

        index = self.product.findData(self.movement.product_id)
        if index >= 0:
            self.product.setCurrentIndex(index)

        if self.movement.type.value == "in":
            self.rb_in.setChecked(True)
        else:
            self.rb_out.setChecked(True)

    def on_save(self):
        if self.product.currentIndex() < 0:
            QMessageBox.warning(self, "Warning", "No product selected")
            return

        if not self.quantity.text().strip():
            QMessageBox.warning(self, "Warning", "The quantity was not specified")
            return

        try:
            quantity = int(self.quantity.text())
            if quantity <= 0:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Warning", "Quantity must be a positive number")
            return

        if not (self.rb_in.isChecked() or self.rb_out.isChecked()):
            QMessageBox.warning(self, "Warning", "Select movement type")
            return

        self.accept()

    def get_data(self):
        return {
            "product_id": self.product.currentData(),
            "quantity": int(self.quantity.text()),
            "type": "in" if self.rb_in.isChecked() else "out",
            "note": self.note.toPlainText().strip(),
        }
