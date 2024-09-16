import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

class VentanaNombreEdad(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()

    def inicializar_ui(self):
        self.setWindowTitle('Nombre y Edad')
        self.setGeometry(100, 100, 300, 200)

        # Crear un layout
        layout = QVBoxLayout()

        # Crear los labels para mostrar el nombre y la edad
        nombre = QLabel('Nombre Completo: Pepe Juan Suarez A Tercero', self)
        edad = QLabel('Edad: 16', self)

        # Alinear texto al centro
        nombre.setAlignment(Qt.AlignCenter)
        edad.setAlignment(Qt.AlignCenter)

        # Agregar los widgets al layout
        layout.addWidget(nombre)
        layout.addWidget(edad)

        # Asignar el layout al QWidget
        self.setLayout(layout)

# Ejecutar la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaNombreEdad()
    ventana.show()
    sys.exit(app.exec_())
