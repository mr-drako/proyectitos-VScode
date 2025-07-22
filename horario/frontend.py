from PyQt5.QtWidgets import (QWidget, QPushButton, QVBoxLayout, QHBoxLayout,
                             QTableWidget, QTableWidgetItem, QListWidget,
                             QListWidgetItem)
from PyQt5.QtCore import pyqtSignal, Qt


class Main_Window(QWidget):

    senal_data = pyqtSignal(list)
    senal_opciones = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self.UI()

    def UI(self) -> None:
        # Geometria de la ventana
        ancho_ventana = 1200
        largo_ventana = 600
        x_ventana = (1920 - ancho_ventana) // 2
        y_ventana = (1080 - largo_ventana) // 2
        self.setGeometry(x_ventana, y_ventana, ancho_ventana, largo_ventana)
        self.setWindowTitle("Horarios Oficina")

        # Widgets
        self.nombres = QListWidget(self)
        self.horario = QTableWidget(6, 5, self)
        self.horario.setMinimumSize(752, 600)
        self.horario.setHorizontalHeaderLabels(["Lunes", "Martes", "Miercoles",
                                                "Jueves", "Viernes"])
        for row in range(self.horario.rowCount()):
            self.horario.setRowHeight(row, 93)
        self.horario.verticalHeader().setVisible(False)
        self.boton = QPushButton('Generar horario', self)
        self.boton.clicked.connect(self.selecciones)

        # Layouts
        vbox_1 = QVBoxLayout()
        vbox_1.addStretch(1)
        vbox_1.addWidget(self.nombres)
        vbox_1.addSpacing(10)
        vbox_1.addWidget(self.boton)
        vbox_1.addStretch(1)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.horario)
        hbox.addStretch(1)
        hbox.addLayout(vbox_1)
        hbox.addStretch(1)

        vbox_2 = QVBoxLayout()
        vbox_2.addStretch(1)
        vbox_2.addLayout(hbox)
        vbox_2.addStretch(1)

        self.setLayout(vbox_2)

    def opciones(self, files: list) -> None:
        files.append("Todos.txt")
        for i in range(len(files)):
            item = QListWidgetItem(f"{files[i][:-4]}")
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            self.nombres.addItem(item)
        self.nombres.itemChanged.connect(self.check_todos)

    def check_todos(self, item: QListWidgetItem) -> None:
        if item.text() == "Todos":
            self.nombres.itemChanged.disconnect(self.check_todos)
            ticket = item.checkState()
            for i in range(self.nombres.count()):
                new_item = self.nombres.item(i)
                if new_item.text() != "Todos":
                    new_item.setCheckState(ticket)
            self.nombres.itemChanged.connect(self.check_todos)

    def selecciones(self) -> None:
        elegidos = []
        for i in range(self.nombres.count()):
            item = self.nombres.item(i)
            if item.checkState() == 2 and item.text() != "Todos":
                elegidos.append(item.text())
        self.senal_data.emit(elegidos)

    def generar_horario(self, datos: list) -> None:
        self.horario.clear()
        self.horario.setHorizontalHeaderLabels(["Lunes", "Martes", "Miercoles",
                                                "Jueves", "Viernes"])
        for row in range(self.horario.rowCount()):
            for col in range(self.horario.columnCount()):
                if self.horario.item(row, col) is None:
                    self.horario.setItem(row, col, QTableWidgetItem(""))
        for data in datos:
            nombre, horas = data
            for row, col in horas:
                item = self.horario.item(row, col)
                item.setText(item.text() + nombre + "\n")
