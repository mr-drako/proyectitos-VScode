import os
import sys
import tkinter as tk
import ctypes
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QLineEdit, QHBoxLayout, QVBoxLayout, 
                             QGridLayout)
from PyQt5.QtCore import (QCoreApplication, pyqtSignal, QSize, Qt)
from PyQt5.QtGui import (QMouseEvent, QKeyEvent, QPixmap, QIcon, QResizeEvent)

class BotonImagen(QLabel):

    senal_presionado = pyqtSignal(int)

    def __init__(self, radio: int, imagen: QPixmap, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.radio = radio
        self.imagen = imagen
        self.senal_presionado.connect(lambda r: print(f"el radio elegido es de {r} pixeles"))
        self.ajustar_tamaño()
    
    def ajustar_tamaño(self) -> None:
        tamano = 2 * self.radio
        imagen_escalada = self.imagen.scaled(
            tamano, tamano,
            Qt.KeepAspectRatio, 
            Qt.SmoothTransformation
        )
        self.setPixmap(imagen_escalada)
        self.setFixedSize(tamano, tamano)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.senal_presionado.emit(self.radio)

class Listo(QLabel):

    senal_listo = pyqtSignal()

    def __init__(self, imagen: QPixmap, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.imagen = imagen
        self.ajustar_tamaño()
        self.senal_listo.connect(lambda : print("funciona"))

    def ajustar_tamaño(self) -> None:
        imagen_escalada = self.imagen.scaled(
            150, 30,
            Qt.KeepAspectRatio, 
            Qt.SmoothTransformation
        )
        self.setPixmap(imagen_escalada)
        self.setFixedSize(150, 30)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.senal_listo.emit()
        

class Ventana(QWidget):
    
    def __init__(self, coordenadas: tuple, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.coordenadas = coordenadas
        self.init_gui()
        self.show()
    
    def init_gui(self) -> None:

        self.setGeometry(*self.coordenadas, 850, 500)
        self.setWindowTitle("Urna")
        ruta_fondo = os.path.join("imagenes_frontend", "fondo_urna.png")
        self.fondo = QLabel(self)
        self.fondo.setGeometry(0, 0, 1024, 576)
        fondo = QPixmap(ruta_fondo)
        self.fondo.setPixmap(fondo)
        self.fondo.setScaledContents(True)

        ruta_particula = os.path.join("imagenes_frontend", "particula.png")
        self.boton_particula_10 = BotonImagen(10, QPixmap(ruta_particula), self)
        self.boton_particula_25 = BotonImagen(25, QPixmap(ruta_particula), self)
        self.boton_particula_10.resize(20, 20)
        self.placeholder_2 = QLabel("cantidad particulas", self)
        self.placeholder_3 = QLabel("tamaño particulas", self)
        self.barra_texto = QLineEdit()
        self.barra_texto.setStyleSheet("""
        QLineEdit {
        background-image: url(imagenes_frontend\barra.png);
        background-repeat: no-repeat; 
        background-position: center;
        color: white;  black
        }
        """)
        ruta_listo = os.path.join("imagenes_frontend", "listo_termo")
        self.boton_listo = Listo(QPixmap(ruta_listo), self)

        #Layout
        
        hbox_1 = QHBoxLayout()
        hbox_1.addStretch(1)
        hbox_1.addWidget(self.placeholder_2)
        hbox_1.addStretch(1)
        hbox_1.addWidget(self.placeholder_3)
        hbox_1.addStretch(1)

        hbox_2 = QHBoxLayout()
        hbox_2.addStretch(1)
        hbox_2.addWidget(self.barra_texto)
        hbox_2.addStretch(1)
        hbox_2.addWidget(self.boton_particula_10)
        hbox_2.addSpacing(20)
        hbox_2.addWidget(self.boton_particula_25)
        hbox_2.addStretch(1)

        hbox_final = QHBoxLayout()
        hbox_final.addStretch(2)
        hbox_final.addSpacing(80)
        hbox_final.addWidget(self.boton_listo)
        hbox_final.addStretch(2)
        
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox_1)
        vbox.addSpacing(30)
        vbox.addLayout(hbox_2)
        vbox.addStretch(1)
        vbox.addLayout(hbox_final)
        vbox.addStretch(1)

        self.setLayout(vbox)
        self.fondo.lower()

    
    def resizeEvent(self, event: QResizeEvent) -> None:
        self.fondo.setGeometry(0, 0, self.width(), self.height())
        return super().resizeEvent(event)

if __name__ == '__main__':
    #do the frontend shit
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