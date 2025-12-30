from PySide6.QtWidgets import QDialog, QLineEdit, QTextEdit, QPushButton, QFormLayout, QVBoxLayout, QMessageBox, \
    QHBoxLayout


class CategoryForm(QDialog):
    def __init__(self, parent=None, category=None):
        super().__init__(parent)

        self.category = category
        self.is_edit = category is not None

        self.setWindowTitle("Edit Category" if self.is_edit else "New Category")
        self.setModal(True)

        self.name = QLineEdit()
        self.description = QTextEdit()

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

        buttons = QHBoxLayout()
        buttons.addStretch()
        buttons.addWidget(btn_save)
        buttons.addWidget(btn_cancel)

        main = QVBoxLayout()
        main.addLayout(form)
        main.addLayout(buttons)

        self.setLayout(main)

    def load_data(self):
        self.name.setText(self.category.name)
        self.description.setPlainText(self.category.description or "")

    def on_save(self):
        if not self.name.text().strip():
            QMessageBox.warning(self, "Validation error", "Name is required")
            return

        self.accept()

    def get_data(self):
        return {
            "name": self.name.text().strip(),
            "description": self.description.toPlainText().strip(),
        }