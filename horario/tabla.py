from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import (QWidget, QTableWidget,
                             QTableWidgetItem, QVBoxLayout)
from PyQt5.QtWidgets import QApplication
import sys


class Backend(QObject):
    # Señal que envía datos al frontend (un lote de filas)
    senal_datos_tabla = pyqtSignal(list)

    def generar_datos(self):
        """Generador que simula datos (ej: consulta a BD o API)"""
        for i in range(1, 101):  # 100 filas de ejemplo
            # Cada fila es una lista (ej: [id, nombre, valor])
            fila = [i, f"Item {i}", i * 10]
            yield fila

    def enviar_a_tabla(self):
        """Envía datos del generador a la tabla por lotes (para eficiencia)"""
        generador = self.generar_datos()
        lote = []
        for fila in generador:
            lote.append(fila)
            if len(lote) >= 20:  # Enviar cada 20 filas
                self.senal_datos_tabla.emit(lote)
                lote = []
        if lote:  # Enviar las filas restantes
            self.senal_datos_tabla.emit(lote)


class VentanaPrincipal(QWidget):
    def __init__(self, backend):
        super().__init__()
        self.backend = backend
        self.init_ui()
        self.conectar_señales()

    def init_ui(self):
        self.tabla = QTableWidget(self)
        self.tabla.setColumnCount(3)
        self.tabla.setHorizontalHeaderLabels(["ID", "Nombre", "Valor"])

        layout = QVBoxLayout()
        layout.addWidget(self.tabla)
        self.setLayout(layout)

    def conectar_señales(self):
        self.backend.senal_datos_tabla.connect(self.actualizar_tabla)

    def actualizar_tabla(self, filas):
        """Añade filas a la tabla desde una lista"""
        row_count = self.tabla.rowCount()
        self.tabla.setRowCount(row_count + len(filas))

        for i, fila in enumerate(filas):
            for j, dato in enumerate(fila):
                self.tabla.setItem(row_count + i, j,
                                   QTableWidgetItem(str(dato)))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    backend = Backend()
    ventana = VentanaPrincipal(backend)
    ventana.show()

    # Iniciar el envío de datos (puede ser desde un botón)
    backend.enviar_a_tabla()

    sys.exit(app.exec_())
