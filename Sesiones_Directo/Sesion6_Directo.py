from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QApplication, QWidget, QLabel


class Interfaz1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interfaz 1")

        # Layout
        layout = QVBoxLayout()
        self.input = QLineEdit()
        self.btn = QPushButton("Pasar de interfaz")
        # Conectar el metodo a este boton
        self.btn.clicked.connect(self.pasar_interfaz)

        layout.addWidget(self.input)
        layout.addWidget(self.btn)

        self.setLayout(layout)

    def pasar_interfaz(self):
        # Esto es para mostrar la interfaz 2
        # Mediante la instancia con la que se crea la clase aqui le pasamos el texto que esta en el QLine
        self.ventana = Interfaz2(self.input.text())
        self.ventana.show()

        self.close()



class Interfaz2(QWidget):
    # Siempre que querais pasar argumentos de una interfaz a otra se pasan mediante el constructor
    def __init__(self, lbl_text):
        super().__init__()
        self.setWindowTitle("Interfaz 2")

        # Layout
        layout = QVBoxLayout()
        # Le paso mediante el constructor el texto que quiero que figure en el label
        self.lbl = QLabel(lbl_text)
        self.btn_regresar = QPushButton("Regresar a la primera interfaz")
        self.btn_regresar.clicked.connect(self.regresar_interfaz)

        layout.addWidget(self.lbl)
        layout.addWidget(self.btn_regresar)

        self.setLayout(layout)

    def regresar_interfaz(self):
        self.ventana_principal = Interfaz1()
        self.ventana_principal.show()
        self.close()

if __name__ == "__main__":
    app = QApplication()
    interfaz1 = Interfaz1()
    interfaz1.show()
    app.exec()