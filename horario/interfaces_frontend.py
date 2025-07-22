import os
import sys
import tkinter as tk
import ctypes
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QLineEdit, QHBoxLayout, QVBoxLayout, 
                             QGridLayout)
from PyQt5.QtCore import (QCoreApplication, pyqtSignal, QSize)
from PyQt5.QtGui import (QMouseEvent, QKeyEvent, QPixmap, QIcon, QResizeEvent) 

class BotonImagen(QLabel):

    senal_presionado = pyqtSignal(int)

    def __init__(self, tiempo: int, imagen: QPixmap, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.tiempo = tiempo 
        self.setPixmap(imagen)
        self.senal_presionado.connect(lambda t: print(f"boton presionado tiempo: {t} segundos"))
    
    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.senal_presionado.emit(self.tiempo)

class Boton(QPushButton):

    senal_presionado = pyqtSignal(int)

    def __init__(self, tiempo: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tiempo = tiempo
        self.clicked.connect(self.presionar)

    def presionar(self) -> None:
        print(f"boton presionado de {self.tiempo} segundos")
        self.senal_presionado.emit(self.tiempo)

class Ventana(QWidget):
    
    def __init__(self, coordenadas: tuple, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.coordenadas = coordenadas
        self.init_gui()
        self.show()
    
    def init_gui(self) -> None:

        self.setGeometry(*self.coordenadas, 850, 500)
        self.setWindowTitle("interfaz")
        ruta_icon = os.path.join("archivos", "interfaces", "icono_huevo.png")
        self.setWindowIcon(QIcon(ruta_icon))
        
        self.fondo = QLabel(self)
        self.fondo.setGeometry(0, 0, 850, 500)
        ruta_fondo = os.path.join("archivos", "interfaces",
                                  "background_ventana.png")
        fondo = QPixmap(ruta_fondo)
        self.fondo.setPixmap(fondo)
        self.fondo.setScaledContents(True)

        ruta_icon_boton1 = os.path.join("archivos", "interfaces", "huevo_test_30.png")
        self.boton1 = BotonImagen(30, QPixmap(ruta_icon_boton1), self)
        
        ruta_icon_boton2 = os.path.join("archivos", "interfaces", "pollo_test_2.png")
        self.boton2 = BotonImagen(60, QPixmap(ruta_icon_boton2), self)

        self.boton3 = Boton(90, "test 90s", self)
        self.boton4 = Boton(120, "test 120s", self)

        hbox_1 = QHBoxLayout()
        hbox_1.addStretch(1)
        hbox_1.addWidget(self.boton1)
        hbox_1.addStretch(1)
        hbox_1.addWidget(self.boton2)
        hbox_1.addStretch(1)

        hbox_2 = QHBoxLayout()
        hbox_2.addStretch(1)
        hbox_2.addWidget(self.boton3)
        hbox_2.addStretch(1)
        hbox_2.addWidget(self.boton4)
        hbox_2.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox_1)
        vbox.addStretch(1)
        vbox.addLayout(hbox_2)
        vbox.addStretch(1)
        
        self.setLayout(vbox)
        self.fondo.lower()

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.fondo.setGeometry(0, 0, self.width(), self.height())
        return super().resizeEvent(event)




if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    
    raiz = tk.Tk()
    ancho = raiz.winfo_screenwidth()
    largo = raiz.winfo_screenheight()
    raiz.destroy()
    ancho_final = int((ancho - 850) / 2)
    largo_final = int((largo - 500) / 2)
   
    app = QApplication([])
    ventana = Ventana((ancho_final, largo_final))
    sys.exit(app.exec())

