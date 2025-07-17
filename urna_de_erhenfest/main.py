import sys
from PyQt5.QtWidgets import QApplication
from frontend_urna import Ventana
from urna import urna


if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication([])
    ventana = Ventana()
    ventana.show()
    ventana.senal_inicio.connect(urna)
    app.exec_()
