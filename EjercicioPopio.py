# En este Ejercicio se decidio crear un programa que muestre tres opciones de comida
# y que se agrege la cantidad de comida seleccionada
# para esto se uso el widget de Spinbox y Radio box 
# ademas de utilizarse el widget de MensageBox para el mensaje de confirmacion
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QSpinBox, QLabel, QPushButton, QMessageBox

class VentanaRadioSpinBox(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()

    def inicializar_ui(self):
        self.setWindowTitle('Ejercicio Propio')
        self.setGeometry(100, 100, 300, 200)

        # Crear layout principal
        layout = QVBoxLayout()

        # Etiqueta de instrucciones
        self.label_opcion = QLabel('Selecciona una opción de comida:')
        layout.addWidget(self.label_opcion)

        # Crear botones de opción (RadioButton)
        self.radio1 = QRadioButton('Pizza', self)
        self.radio2 = QRadioButton('Hamburguesa', self)
        self.radio3 = QRadioButton('Burritos', self)

        # Agregar los RadioButtons al layout
        layout.addWidget(self.radio1)
        layout.addWidget(self.radio2)
        layout.addWidget(self.radio3)

        # SpinBox para seleccionar cantidad
        self.spin_box = QSpinBox(self)
        self.spin_box.setRange(1, 20)  # Rango de valores de 1 a 20
        self.spin_box.setValue(1)      # Valor inicial en 1
        layout.addWidget(QLabel('Selecciona la cantidad:'))
        layout.addWidget(self.spin_box)

        # Botón para confirmar
        boton_confirmar = QPushButton('Confirmar pedido', self)
        boton_confirmar.clicked.connect(self.mostrar_pedido)

        # Agregar el botón al layout
        layout.addWidget(boton_confirmar)

        # Establecer el layout
        self.setLayout(layout)

    def mostrar_pedido(self):
        # Comprobar qué opción de comida está seleccionada
        if self.radio1.isChecked():
            comida_seleccionada = 'Pizza'
        elif self.radio2.isChecked():
            comida_seleccionada = 'Hamburguesa'
        elif self.radio3.isChecked():
            comida_seleccionada = 'Burritos'
        else:
            comida_seleccionada = 'Nada seleccionado'

        # Obtener la cantidad seleccionada del SpinBox
        cantidad = self.spin_box.value()

        # Mostrar un mensaje con el pedido
        mensaje = f"Has pedido {cantidad} {comida_seleccionada}(s)."
        QMessageBox.information(self, 'Pedido', mensaje)

# Ejecutar la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaRadioSpinBox()
    ventana.show()
    sys.exit(app.exec_())
