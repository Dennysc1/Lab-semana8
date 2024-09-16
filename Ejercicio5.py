from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout
import sys

def leer_datos_persona():
    app = QApplication(sys.argv)
    ventana = QWidget()
    ventana.setWindowTitle('Datos Característicos')

    # Crear el layout
    layout = QVBoxLayout()
    
    # Crear entradas para los 10 datos
    for i in range(10):
        etiqueta_dato = QLabel(f'Dato {i + 1}:')
        entrada_dato = QLineEdit()
        
        layout.addWidget(etiqueta_dato)
        layout.addWidget(entrada_dato)

    ventana.setLayout(layout)
    ventana.resize(400, 500)
    ventana.show()
    sys.exit(app.exec_())

leer_datos_persona()
