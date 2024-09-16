import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QLineEdit, QPushButton

class VentanaCedula(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()

    def inicializar_ui(self):
        self.setWindowTitle('Número de DUI y Nombre')
        self.setGeometry(100, 100, 300, 200)

        # Crear un layout
        layout = QVBoxLayout()

        # Campos de texto
        label_cedula = QLabel('Introduce tu número de DUI:', self)
        self.campo_cedula = QLineEdit(self)

        label_nombre = QLabel('Introduce tu nombre completo:', self)
        self.campo_nombre = QLineEdit(self)

        # Botón de envío
        boton_enviar = QPushButton('Enviar', self)
        boton_enviar.clicked.connect(self.mostrar_datos)

        # Agregar widgets al layout
        layout.addWidget(label_cedula)
        layout.addWidget(self.campo_cedula)
        layout.addWidget(label_nombre)
        layout.addWidget(self.campo_nombre)
        layout.addWidget(boton_enviar)

        # Asignar layout
        self.setLayout(layout)

    def mostrar_datos(self):
        cedula = self.campo_cedula.text()
        nombre = self.campo_nombre.text()
        print(f"DUI: {cedula}, Nombre: {nombre}")  # Mostrar en consola

# Ejecutar la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaCedula()
    ventana.show()
    sys.exit(app.exec_())
