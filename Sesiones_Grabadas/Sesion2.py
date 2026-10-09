from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QMainWindow


class Contador(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Contador")

        # Un texto que represente un numero
        # Un boton que lo que haga es incrementar
        # Un boton que lo que haga es decrementar
        # Un boton que lo que haga es resetear

        self.lbl_numero = QLabel("0")
        btn_incrementar = QPushButton("Incrementar")
        btn_incrementar.clicked.connect(lambda : self.sumar_restar(1))
        # Es necesario la funcion lamda para los eventos porque si no se consigue una instancia
        # del propio método que hace que congele mi interfaz
        btn_decrementar = QPushButton("Decrementar")
        btn_decrementar.clicked.connect(lambda: self.sumar_restar(-1))
        btn_resetear = QPushButton("Resetear")
        btn_resetear.clicked.connect(lambda: self.sumar_restar(-int(self.lbl_numero.text())))

        # Manera en la que organizo la interfaz
        layout = QVBoxLayout()
        layout.addWidget(self.lbl_numero)
        layout.addWidget(btn_incrementar)
        layout.addWidget(btn_decrementar)
        layout.addWidget(btn_resetear)

        self.setLayout(layout)

    def sumar_restar(self, numero):
        contador = int(self.lbl_numero.text())
        self.lbl_numero.setText(str(contador + numero))

# Defino una clase semaforo que es otra interfaz.
class Semaforo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Semaforo")

        # Estados posibles
        self.estados = ["ROJO", "AMARILLO", "VERDE"]
        self.estado_actual = 0

        # Luces
        self.luz_roja = QLabel()
        self.luz_amarilla = QLabel()
        self.luz_verde = QLabel()

        for luz in (self.luz_roja, self.luz_amarilla, self.luz_verde):
            luz.setFixedSize(100, 100)
            luz.setStyleSheet("background-color: grey; border-radius: px;")

        # Boton
        self.boton = QPushButton("Cambiar")
        self.boton.clicked.connect(self.cambiar_estado)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.luz_roja)
        layout.addWidget(self.luz_amarilla)
        layout.addWidget(self.luz_verde)
        layout.addWidget(self.boton)

        self.setLayout(layout)
        self.actualizar_luces()

    def actualizar_luces(self):
        # Apago todas
        self.luz_roja.setStyleSheet("background-color: grey; border-radius: px;")
        self.luz_amarilla.setStyleSheet("background-color: grey; border-radius: px;")
        self.luz_verde.setStyleSheet("background-color: grey; border-radius: px;")

        estado = self.estados[self.estado_actual]
        if estado == "ROJO":
            self.luz_roja.setStyleSheet("background-color: red; border-radius: px;")
        elif estado == "AMARILLO":
            self.luz_amarilla.setStyleSheet("background-color: yellow; border-radius: px;")
        else:
            self.luz_verde.setStyleSheet("background-color: green; border-radius: px;")

    def cambiar_estado(self):
        self.estado_actual = (self.estado_actual + 1) % 3
        self.actualizar_luces()

if __name__ == "__main__":
    app = QApplication([])
    semaforo = Semaforo()
    semaforo.show()
    app.exec()