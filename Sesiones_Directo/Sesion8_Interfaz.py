from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication, QMessageBox

from Sesion8_BtnPersonalizado import BotonPersonalizado
class Interfaz(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo de boton personalizado")

        self.boton = BotonPersonalizado("Enviar", "#2563EB")
        self.boton.clicked.connect(self.mostrar_aviso)

        layout = QVBoxLayout(self)
        layout.addWidget(self.boton)

    def mostrar_aviso(self):
        QMessageBox.information(self, "Boton pulsado", f"Has pulsado el boton {self.boton.text()}")

if __name__ == "__main__":
    app = QApplication()
    interfaz = Interfaz()
    interfaz.show()
    app.exec()