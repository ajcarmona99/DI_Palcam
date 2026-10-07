from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QLineEdit, QWidget, QPushButton, QLabel


class CalculadoraDescuento(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora con descuento")

        layout = QVBoxLayout()
        self.label_precio = QLineEdit()
        self.label_descuento = QLineEdit()
        self.btn_descuento = QPushButton("Hacer descuento")
        self.btn_descuento.clicked.connect(self.calcular)
        self.lbl_hecho_descuento = QLabel()

        layout.addWidget(self.label_precio)
        layout.addWidget(self.label_descuento)
        layout.addWidget(self.btn_descuento)
        layout.addWidget(self.lbl_hecho_descuento)
        self.setLayout(layout)

    def calcular(self):
        try:
            precio = float(self.label_precio.text())
            descuento = float(self.label_descuento.text())

            precio_final = precio - (precio * descuento / 100)
            self.lbl_hecho_descuento.setText((f"Precio final: {precio_final}"))
        except ValueError:
            self.lbl_hecho_descuento.setText("Hay algo que no es un número")

if __name__ == "__main__":
    app = QApplication([])
    calculadora = CalculadoraDescuento()
    calculadora.show()
    app.exec()