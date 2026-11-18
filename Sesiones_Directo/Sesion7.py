from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QWidget, QApplication, QHBoxLayout, QLabel, QVBoxLayout, QPushButton


# Se hereda de la clase QWidget porque es la que representa una interfaz en PySide6
# y es lo más sencillo de programar si no me pide un menú superior
class Cronometro(QWidget):
    def __init__(self):
        # Llamo al constructor de la clase padre
        super().__init__()
        # Establezco un titulo a la ventana
        self.setWindowTitle("Cronometro")
        # Establezco las dimensiones cotidianas de un cronometros
        self.resize(250, 150)

        # Un cronometro se representa en PySide6 como un QTimer
        self.timer = QTimer(self)
        self.segundos = 0
        self.timer.timeout.connect(self.actualizar_tiempo)

        # Establezco el label de los botones y los botones para iniciar, pausar, reiniciar
        layout = QHBoxLayout()
        self.label_tiempo = QLabel("00:00")
        # Establezcco unos estilos al cronometro
        self.label_tiempo.setStyleSheet("font-size:24px; color:blue; text-align:center;")

        # Ahora los botones
        layout_btn = QVBoxLayout()
        self.btn_iniciar = QPushButton("Iniciar")
        self.btn_iniciar.clicked.connect(self.iniciar)
        self.btn_pausar = QPushButton("Pausar")
        self.btn_pausar.clicked.connect(self.pausar)
        self.btn_reiniciar = QPushButton("Reiniciar")
        self.btn_reiniciar.clicked.connect(self.reiniciar)

        layout_btn.addWidget(self.btn_iniciar)
        layout_btn.addWidget(self.btn_pausar)
        layout_btn.addWidget(self.btn_reiniciar)

        layout.addWidget(self.label_tiempo)
        layout.addLayout(layout_btn)

        self.setLayout(layout)

    def iniciar(self):
        if not self.timer.isActive():
            self.timer.start(1000)


    def pausar(self):
        # Si el temporizador esta activo
        if self.timer.isActive():
            self.timer.stop()

    def reiniciar(self):
        # Se para el temporizador
        self.timer.stop()
        # Los segundos se establecen en 0
        self.segundos = 0
        # El label del tiempo se establece en 00:00
        self.label_tiempo.setText("00:00")


    def actualizar_tiempo(self):
        self.segundos +=1
        minutos, segundos = divmod(self.segundos, 60)
        self.label_tiempo.setText(f"{minutos:02}:{segundos:02}")

# Si ejecuto este archivo
if __name__ == "__main__":
    app = QApplication()
    interfaz = Cronometro()
    interfaz.show()
    app.exec()