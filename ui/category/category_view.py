from PySide6.QtWidgets import QWidget, QTableWidget, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout


class CategoryView(QWidget):
    def __init__(self):
        super().__init__()

        self.table = QTableWidget()
        self.btn_add = QPushButton('Add')
        self.btn_edit = QPushButton('Edit')
        self.btn_delete = QPushButton('Delete')
        self.search = QLineEdit()
        self.search.setPlaceholderText("Category search...")

        layout = QVBoxLayout()
        toolbar = QHBoxLayout()

        toolbar.addWidget(self.search)
        toolbar.addWidget(self.btn_add)
        toolbar.addWidget(self.btn_edit)
        toolbar.addWidget(self.btn_delete)

        layout.addLayout(toolbar)
        layout.addWidget(self.table)

        self.setLayout(layout)