from PySide6.QtWidgets import QWidget, QApplication, QHBoxLayout, QLabel, QLineEdit, QPushButton


class Interfaz(QWidget):
    # Inicializo el constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Contador")

        # Como tengo que introducir objetos voy a utilizar un layout para disponer los elementos
        # en la interfaz
        layout = QHBoxLayout()
        # Defino los elementos que quiere la interfaz
        self.label_contador = QLabel("0")
        self.input = QLineEdit()
        self.btn_incrementar = QPushButton("Incrementar")
        self.btn_incrementar.clicked.connect(lambda : self.sumar_restar(True))
        self.btn_decrementar = QPushButton("Decrementar")
        self.btn_decrementar.clicked.connect(lambda : self.sumar_restar(False))
        # Lo mismo que restar el número
        self.btn_decrementar.clicked.connect(self.sumar_restar)
        # Añado estos elementos al layout
        layout.addWidget(self.label_contador)
        layout.addWidget(self.input)
        layout.addWidget(self.btn_incrementar)
        layout.addWidget(self.btn_decrementar)

        # Establezco el layout a la interfaz
        self.setLayout(layout)

        # Establezco el control de colores
        self.controlar_color()

    def sumar_restar(self, sumar):
        try:
            # Sirve como comprobacion para ver si lo que introduce es un numero
            contador = int(self.label_contador.text())
            numero_sumado = int(self.input.text())
            if sumar:
                # Hago la suma al numero
                resultado = contador + numero_sumado
            else:
                resultado = contador - numero_sumado
            self.label_contador.setText(str(resultado))
            self.controlar_color()
        except ValueError:
            self.label_contador.setText("Tienes que introducir un numero")

    def controlar_color(self):
        contador = int(self.label_contador.text())
        if contador > 0:
            self.label_contador.setStyleSheet("QLabel {color:green;}")
        elif contador < 0:
            self.label_contador.setStyleSheet("QLabel {color: red;}")
        else:
            self.label_contador.setStyleSheet("QLabel {color: yellow; }")
# public static void
if __name__ == "__main__":
    app = QApplication([])
    interfaz = Interfaz()
    interfaz.show()
    app.exec()