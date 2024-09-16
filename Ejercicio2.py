from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt
import sys

def leer_clave():
    app = QApplication(sys.argv)
    ventana = QWidget()
    ventana.setWindowTitle('Clave Secreta')

    # Crear el layout, etiqueta y entrada
    layout = QVBoxLayout()
    
    etiqueta = QLabel('Ingrese su clave:')
    etiqueta.setAlignment(Qt.AlignCenter)  # Centrar la etiqueta
    
    entrada_clave = QLineEdit()
    entrada_clave.setEchoMode(QLineEdit.Password)  # Ocultar los caracteres
    
    layout.addWidget(etiqueta)
    layout.addWidget(entrada_clave)
    ventana.setLayout(layout)
    
    ventana.resize(300, 150)
    ventana.show()
    sys.exit(app.exec_())

leer_clave()
