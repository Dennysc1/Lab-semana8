from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout
import sys

def leer_mascotas():
    app = QApplication(sys.argv)
    ventana = QWidget()
    ventana.setWindowTitle('Datos de Mascotas')

    # Crear el layout
    layout = QVBoxLayout()
    
    # Crear entradas para las 3 mascotas
    for i in range(3):
        etiqueta_mascota = QLabel(f'Mascota {i + 1} - Nombre, Edad, Tipo:')
        entrada_mascota = QLineEdit()
        
        layout.addWidget(etiqueta_mascota)
        layout.addWidget(entrada_mascota)

    ventana.setLayout(layout)
    ventana.resize(400, 300)
    ventana.show()
    sys.exit(app.exec_())

leer_mascotas()
