import sys
from PyQt5.QtWidgets import QApplication
from frontend import Main_Window
from backend import Funciones

if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication([])
    ventana = Main_Window()
    funciones = Funciones()
    ventana.senal_opciones.connect(funciones.data_horarios)
    funciones.emisor_opciones.connect(ventana.opciones)
    ventana.senal_data.connect(funciones.disponibilidad)
    funciones.emisor_data.connect(ventana.generar_horario)
    ventana.senal_opciones.emit()
    ventana.show()
    sys.exit(app.exec_())
