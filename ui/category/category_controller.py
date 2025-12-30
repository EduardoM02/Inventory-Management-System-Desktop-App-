from PySide6.QtWidgets import QTableWidgetItem, QMessageBox, QTableWidget, QHeaderView

from ui.category.category_form import CategoryForm


class CategoryController:
    def __init__(self, view, service):
        self.view = view
        self.service = service

        self.view.btn_add.clicked.connect(self.add_category)
        self.view.btn_edit.clicked.connect(self.edit_category)
        self.view.btn_delete.clicked.connect(self.delete_category)
        self.view.table.cellDoubleClicked.connect(self.on_table_double_click)
        self.view.search.textChanged.connect(self.on_search)

        self.setup_table()
        self.load_table()

    def setup_table(self):
        self.view.table.setColumnCount(3)
        self.view.table.setHorizontalHeaderLabels(['ID', 'Name', 'Description'])
        self.view.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.view.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.view.table.setSelectionMode(QTableWidget.SingleSelection)
        header = self.view.table.horizontalHeader()
        header.setStretchLastSection(False)
        header.setSectionResizeMode(2, QHeaderView.Stretch)

    def fill_table(self, categories):
        self.view.table.setRowCount(len(categories))

        for row, category in enumerate(categories):
            self.view.table.setItem(row, 0, QTableWidgetItem(str(category['id'])))
            self.view.table.setItem(row, 1, QTableWidgetItem(str(category['name'])))
            self.view.table.setItem(row, 2, QTableWidgetItem(str(category['description'])))

    def load_table(self):
        categories = self.service.get_all_categories()
        self.fill_table(categories)
        self.view.table.resizeColumnsToContents()
        self.view.table.clearSelection()

    def on_table_double_click(self, row, column):
        if self.view.table.item(row, 0):
            self.edit_category()

    def on_search(self, text: str):
        if text.strip():
            categories = self.service.search_categories(text)
        else:
            categories = self.service.get_all_categories()

        self.fill_table(categories)
        self.view.table.clearSelection()

    def get_selected_category_id(self):
        selected = self.view.table.currentRow()
        if selected < 0:
            return None
        return int(self.view.table.item(selected, 0).text())

    def add_category(self):
        dialog = CategoryForm(self.view)
        if dialog.exec():
            data = dialog.get_data()

            try:
                self.service.add_category(data)
                self.load_table()
            except ValueError as e:
                QMessageBox.warning(self.view, 'Error', str(e))

    def edit_category(self):
        category_id = self.get_selected_category_id()

        if category_id is None:
            QMessageBox.warning(self.view, "Warning", "Select a category first")
            return

        category = self.service.get_category_by_id(category_id)

        dialog = CategoryForm(self.view, category=category)

        if dialog.exec():
            data = dialog.get_data()
            try:
                self.service.update_category(category_id, data)
                self.load_table()
            except ValueError as e:
                QMessageBox.warning(self.view, "Error", str(e))

    def delete_category(self):
        category_id = self.get_selected_category_id()

        if category_id is None:
            QMessageBox.warning(self.view, "Warning", "Select a category first")
            return

        reply = QMessageBox.question(
            self.view,
            "Confirm delete",
            "Are you sure you want to delete this category?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            try:
                self.service.delete_category(category_id)
                self.load_table()
            except ValueError as e:
                QMessageBox.warning(self.view, "Error", str(e))