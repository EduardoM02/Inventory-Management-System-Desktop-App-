from PySide6.QtWidgets import QAbstractItemView, QTableWidgetItem, QMessageBox, QHeaderView

from ui.movement.movement_form import MovementForm


class MovementController:
    def __init__(self, view, movement_service, product_service):
        self.view = view
        self.service = movement_service
        self.product_service = product_service

        self.view.btn_add.clicked.connect(self.add_movement)
        self.view.btn_edit.clicked.connect(self.edit_movement)
        self.view.btn_delete.clicked.connect(self.delete_movement)
        self.view.table.cellDoubleClicked.connect(self.on_table_double_click)
        self.view.search.textChanged.connect(self.on_search)

        self.setup_table()
        self.load_table()

    def setup_table(self):
        self.view.table.setColumnCount(6)
        self.view.table.setHorizontalHeaderLabels(["ID", "Product", "Type", "Quantity", "Date", "Note"])
        self.view.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.view.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.view.table.setSelectionMode(QAbstractItemView.SingleSelection)
        header = self.view.table.horizontalHeader()
        header.setStretchLastSection(False)
        header.setSectionResizeMode(5, QHeaderView.Stretch)

    def fill_table(self, movements):
        self.view.table.setRowCount(len(movements))

        for row, movement in enumerate(movements):
            self.view.table.setItem(row, 0, QTableWidgetItem(str(movement['id'])))
            self.view.table.setItem(row, 1, QTableWidgetItem(str(movement['product_name'])))
            self.view.table.setItem(row, 2, QTableWidgetItem(str(movement['type'])))
            self.view.table.setItem(row, 3, QTableWidgetItem(str(movement['quantity'])))
            self.view.table.setItem(row, 4, QTableWidgetItem(movement['date'].strftime("%Y-%m-%d %H:%M")))
            self.view.table.setItem(row, 5, QTableWidgetItem(str(movement['note'])))

    def load_table(self):
        movements = self.service.get_all_movements()
        self.fill_table(movements)
        self.view.table.resizeColumnsToContents()
        self.view.table.clearSelection()

    def on_table_double_click(self, row, column):
        if self.view.table.item(row, 0):
            self.edit_movement()

    def on_search(self, text: str):
        if text.strip():
            movements = self.service.search_movement(text)
        else:
            movements = self.service.get_all_movements()

        self.fill_table(movements)
        self.view.table.clearSelection()

    def get_selected_movement_id(self):
        selected = self.view.table.currentRow()
        if selected < 0:
            return None
        return int(self.view.table.item(selected, 0).text())

    def add_movement(self):
        products = self.product_service.get_all_products()
        dialog = MovementForm(self.view, products=products)

        if dialog.exec():
            data = dialog.get_data()
            try:
                self.service.add_movement(data)
                self.load_table()
            except ValueError as e:
                QMessageBox.warning(self.view, "Error", str(e))

    def edit_movement(self):
        movement_id = self.get_selected_movement_id()

        if movement_id is None:
            QMessageBox.warning(self.view, "Warning", "Select a movement first")
            return

        movement = self.service.get_movement_by_id(movement_id)
        products = self.product_service.get_all_products()

        dialog = MovementForm(
            self.view,
            products=products,
            movement=movement,
        )

        if dialog.exec():
            data = dialog.get_data()
            try:
                self.service.update_movement(movement_id, data)
                self.load_table()
            except ValueError as e:
                QMessageBox.warning(self.view, "Error", str(e))

    def delete_movement(self):
        movement_id = self.get_selected_movement_id()

        if movement_id is None:
            QMessageBox.warning(self.view, "Warning", "Select a movement first")
            return

        reply = QMessageBox.question(
            self.view,
            "Confirm Delete",
            "Are you sure you want to delete this movement?",
            QMessageBox.Yes | QMessageBox.No,
        )

        if reply == QMessageBox.Yes:
            try:
                self.service.delete_movement(movement_id)
                self.load_table()
            except ValueError as e:
                QMessageBox.warning(self.view, "Warning", str(e))