import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QLineEdit, QPushButton

class VentanaMascotas(QWidget):
    def __init__(self):  # Corregido: '__init__' con doble guión bajo
        super().__init__()  # Corregido: '__init__' con doble guión bajo
        self.inicializar_ui()

    def inicializar_ui(self):
        self.setWindowTitle('Datos de Mascotas')
        self.setGeometry(100, 100, 300, 300)

        # Crear un layout
        layout = QVBoxLayout()

        # Campos de texto para 3 mascotas
        self.mascota1 = QLineEdit(self)
        self.mascota1.setPlaceholderText('Mascota 1: Nombre, Edad, Raza')

        self.mascota2 = QLineEdit(self)
        self.mascota2.setPlaceholderText('Mascota 2: Nombre, Edad, Raza')

        self.mascota3 = QLineEdit(self)
        self.mascota3.setPlaceholderText('Mascota 3: Nombre, Edad, Raza')

        # Botón de envío
        boton_enviar = QPushButton('Enviar', self)
        boton_enviar.clicked.connect(self.mostrar_datos)

        # Agregar widgets al layout
        layout.addWidget(self.mascota1)
        layout.addWidget(self.mascota2)
        layout.addWidget(self.mascota3)
        layout.addWidget(boton_enviar)

        # Asignar layout
        self.setLayout(layout)

    def mostrar_datos(self):
        datos1 = self.mascota1.text()
        datos2 = self.mascota2.text()
        datos3 = self.mascota3.text()
        print(f"Mascota 1: {datos1}")
        print(f"Mascota 2: {datos2}")
        print(f"Mascota 3: {datos3}")

# Ejecutar la aplicación
if __name__ == '__main__':  # Corregido: '__name__' con doble guión bajo
    app = QApplication(sys.argv)
    ventana = VentanaMascotas()
    ventana.show()
    sys.exit(app.exec_())
