import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton

class DropdownExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Configuración de la ventana
        self.setWindowTitle('Dropdown (QComboBox) en PyQt5')
        self.setGeometry(300, 300, 300, 200)
        
        # Crear layout
        layout = QVBoxLayout()
        
        # Crear etiqueta
        self.label = QLabel("Selecciona una opción:")
        
        # Crear dropdown (QComboBox)
        self.combo = QComboBox()
        
        # Añadir opciones al dropdown
        self.combo.addItem("Selecciona...")  # Opción por defecto
        self.combo.addItem("Opción 1")
        self.combo.addItem("Opción 2")
        self.combo.addItem("Opción 3")
        self.combo.addItems(["Opción 4", "Opción 5"])  # Añadir múltiples items
        
        # Conectar señal de cambio de selección
        self.combo.currentIndexChanged.connect(self.selection_changed)
        
        # Botón para mostrar la selección actual
        self.btn_mostrar = QPushButton("Mostrar selección actual")
        self.btn_mostrar.clicked.connect(self.mostrar_seleccion)
        
        # Añadir widgets al layout
        layout.addWidget(self.label)
        layout.addWidget(self.combo)
        layout.addWidget(self.btn_mostrar)
        
        self.setLayout(layout)
    
    def selection_changed(self, index):
        # Método que se ejecuta cuando cambia la selección
        print(f"Índice seleccionado: {index} - Texto: {self.combo.currentText()}")
    
    def mostrar_seleccion(self):
        # Mostrar la selección actual
        print(f"Selección actual: {self.combo.currentText()}")
        self.label.setText(f"Seleccionaste: {self.combo.currentText()}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DropdownExample()
    window.show()
    sys.exit(app.exec_())