import os
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QLineEdit, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import (pyqtSignal)


class Ventana(QWidget):

    senal_inicio = pyqtSignal(tuple)

    def __init__(self) -> None:
        super().__init__()
        self.iniciar()

    def iniciar(self) -> None:
        # geometria de la ventana
        ancho_ventana = 700
        largo_ventana = 500
        x_ventana = (1920 - ancho_ventana) // 2
        y_ventana = (1080 - largo_ventana) // 2
        self.setGeometry(x_ventana, y_ventana, ancho_ventana, largo_ventana)
        self.setWindowTitle("Urna de ehrenfest")

        # botones y labels
        self.mensaje = QLabel("Ingrese la cantidad de particulas", self)
        self.izq_text = QLabel("Izq:", self)
        self.der_text = QLabel("Der:", self)
        self.izq_edit = QLineEdit('', self)
        self.der_edit = QLineEdit('', self)
        self.boton_inicio = QPushButton('Iniciar', self)
        self.boton_inicio.clicked.connect(self.cierre)

        # layout
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.izq_text)
        hbox.addWidget(self.izq_edit)
        hbox.addStretch(1)
        hbox.addWidget(self.der_text)
        hbox.addWidget(self.der_edit)
        hbox.addStretch(1)

        hbox_2 = QHBoxLayout()
        hbox_2.addStretch(1)
        hbox_2.addWidget(self.mensaje)
        hbox_2.addStretch(1)

        hbox_3 = QHBoxLayout()
        hbox_3.addStretch(1)
        hbox_3.addWidget(self.boton_inicio)
        hbox_3.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox_2)
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        vbox.addLayout(hbox_3)
        vbox.addStretch(1)

        self.setLayout(vbox)

    def cierre(self) -> None:
        izq_text = self.izq_edit.text()
        der_text = self.der_edit.text()
        try:
            izq = int(izq_text)
            der = int(der_text)
            self.senal_inicio.emit((izq, der))
            self.close()
        except (ValueError, TypeError):
            self.mensaje.setText(
                "Error en los valores, reingreselos por favor")


if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication([])
    ventana = Ventana()
    ventana.show()
    app.exec_()
