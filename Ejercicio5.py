import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QLineEdit, QPushButton

class VentanaCaracteristicas(QWidget):
    def __init__(self):  # Corregido: '__init__' con doble guión bajo
        super().__init__()  # Corregido: '__init__' con doble guión bajo
        self.inicializar_ui()

    def inicializar_ui(self):
        self.setWindowTitle('Características de una Persona')
        self.setGeometry(100, 100, 300, 500)

        # Crear un layout
        layout = QVBoxLayout()

        # Campos de texto para 10 características
        self.caracteristicas = [QLineEdit(self) for _ in range(10)]
        for i, caracteristica in enumerate(self.caracteristicas):
            caracteristica.setPlaceholderText(f'Característica {i+1}')
            layout.addWidget(caracteristica)

        # Botón de envío
        boton_enviar = QPushButton('Enviar', self)
        boton_enviar.clicked.connect(self.mostrar_datos)

        # Agregar el botón al layout
        layout.addWidget(boton_enviar)

        # Asignar layout
        self.setLayout(layout)

    def mostrar_datos(self):
        for i, caracteristica in enumerate(self.caracteristicas):
            print(f"Característica {i+1}: {caracteristica.text()}")

# Ejecutar la aplicación
if __name__ == '__main__':  # Corregido: '__name__' con doble guión bajo
    app = QApplication(sys.argv)
    ventana = VentanaCaracteristicas()
    ventana.show()
    sys.exit(app.exec_())
