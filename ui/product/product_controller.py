from PySide6.QtWidgets import QMessageBox, QTableWidgetItem, QAbstractItemView, QHeaderView
from ui.product.product_form import ProductForm


class ProductController:
    def __init__(self, view, product_service, category_service):
        self.view = view
        self.service = product_service
        self.category_service = category_service

        self.view.btn_add.clicked.connect(self.add_product)
        self.view.btn_edit.clicked.connect(self.edit_product)
        self.view.btn_delete.clicked.connect(self.delete_product)
        self.view.table.cellDoubleClicked.connect(self.on_table_double_click)
        self.view.search.textChanged.connect(self.on_search)

        self.setup_table()
        self.load_table()

    def setup_table(self):
        self.view.table.setColumnCount(6)
        self.view.table.setHorizontalHeaderLabels(["ID", "Name", "Category", "Price", "Stock", "Description"])
        self.view.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.view.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.view.table.setSelectionMode(QAbstractItemView.SingleSelection)
        header = self.view.table.horizontalHeader()
        header.setStretchLastSection(False)
        header.setSectionResizeMode(5, QHeaderView.Stretch)

    def fill_table(self, products):
        self.view.table.setRowCount(len(products))

        for row, product in enumerate(products):
            self.view.table.setItem(row, 0, QTableWidgetItem(str(product['id'])))
            self.view.table.setItem(row, 1, QTableWidgetItem(str(product['name'])))
            self.view.table.setItem(row, 2, QTableWidgetItem(str(product['category_name'])))
            self.view.table.setItem(row, 3, QTableWidgetItem(str(product['price'])))
            self.view.table.setItem(row, 4, QTableWidgetItem(str(product['stock'])))
            self.view.table.setItem(row, 5, QTableWidgetItem(str(product['description'])))

    def load_table(self):
        products = self.service.get_all_products()
        self.fill_table(products)
        self.view.table.resizeColumnsToContents()
        self.view.table.clearSelection()

    def on_table_double_click(self, row, column):
        if self.view.table.item(row, 0):
            self.edit_product()

    def on_search(self, text: str):
        if text.strip():
            products = self.service.search_product(text)
        else:
            products = self.service.get_all_products()

        self.fill_table(products)
        self.view.table.clearSelection()

    def get_selected_product_id(self):
        selected = self.view.table.currentRow()
        if selected < 0:
            return None
        return int(self.view.table.item(selected, 0).text())

    def add_product(self):
        categories = self.category_service.get_all_categories()
        dialog = ProductForm(self.view, categories=categories)

        if dialog.exec():
            data = dialog.get_data()
            try:
                self.service.add_product(data)
                self.load_table()
            except ValueError as e:
                QMessageBox.warning(self.view, "Error", str(e))

    def edit_product(self):
        product_id = self.get_selected_product_id()

        if product_id is None:
            QMessageBox.warning(self.view, "Warning", "Select a product first")
            return

        product = self.service.get_product_by_id(product_id)
        categories = self.category_service.get_all_categories()

        dialog = ProductForm(
            self.view,
            categories=categories,
            product=product
        )

        if dialog.exec():
            data = dialog.get_data()
            try:
                self.service.update_product(product_id, data)
                self.load_table()
            except ValueError as e:
                QMessageBox.warning(self.view, "Error", str(e))

    def delete_product(self):
        product_id = self.get_selected_product_id()

        if product_id is None:
            QMessageBox.warning(self.view, "Warning", "Select a product first")
            return

        reply = QMessageBox.question(
            self.view,
            "Confirm delete",
            "Are you sure you want to delete this product?",
            QMessageBox.Yes | QMessageBox.No,
        )

        if reply == QMessageBox.Yes:
            try:
                self.service.delete_product(product_id)
                self.load_table()
            except ValueError as e:
                QMessageBox.warning(self.view, "Warning", str(e))