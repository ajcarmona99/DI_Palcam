import PySide6.QtCore
from PySide6.QtCore import QLine
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QGridLayout, \
    QLineEdit, QSpinBox, QPushButton


class Ejemplo_Grid_QMainWindow(QMainWindow):
    # Creo el constructor
    def __init__(self):
        # Llamo al constructor de la clase padre
        super().__init__()
        # Le pongo un titulo
        self.setWindowTitle("Interfaz de ejemplo")

        # QMainWindow necesita siempre un widget
        widget_central = QWidget()
        self.setCentralWidget(widget_central)

        # Tipo reja o tipo grid
        grid = QGridLayout(widget_central)
        # Añado un texto estatico en la columna 0 y fila 0
        lbl_nombre = QLabel("Nombre: ")
        grid.addWidget(lbl_nombre, 0, 0)

        self.entrada_nombre = QLineEdit()
        self.entrada_nombre.setPlaceholderText("Escribe su nombre:")
        grid.addWidget(self.entrada_nombre, 0, 1)

        grid.addWidget(QLabel("Edad:"), 1, 0)

        self.entrada_edad = QSpinBox()
        self.entrada_edad.setRange(0, 120)
        grid.addWidget(self.entrada_edad, 1, 1)

        self.boton = QPushButton("Mostrar datos")
        self.boton.clicked.connect(self.mostrar_datos)
        grid.addWidget(self.boton, 2, 0, 1, 2)

        self.resultado = QLabel("Completa el formulario")
        grid.addWidget(self.resultado, 3, 0, 1, 2)

        grid.setHorizontalSpacing(15)
        grid.setVerticalSpacing(10)
        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 3)

    def mostrar_datos(self):
        # Tomamos el nombre de la entrada y ademas borramos los espacios
        nombre = self.entrada_nombre.text().strip()
        edad = self.entrada_edad.value()

        if not nombre:
            resultado = "Debes introducir un nombre"
        else:
            resultado = f"Hola, {nombre} tienes esta edad: {edad}"

        self.resultado.setText(resultado)

class Calculadora(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        # Si le queremos establecer un ancho y un alto
        self.setGeometry(100, 100, 300, 400)

        ## Layout principal
        self.layout_principal = QVBoxLayout()
        self.setLayout(self.layout_principal)

        ## Pantalla
        self.pantalla = QLineEdit("")
        self.pantalla.setAlignment(PySide6.QtCore.Qt.AlignmentFlag.AlignRight)
        self.pantalla.setReadOnly(True)
        self.pantalla.setStyleSheet("font-size: 24px;")
        self.layout_principal.addWidget(self.pantalla)

        ## Grid de los botones
        self.grid_layout = QGridLayout()
        self.layout_principal.addLayout(self.grid_layout)

        self.crear_botones()
    def crear_botones(self):
        botones = {
            '7': (0 , 0), '8': (0, 1), '9': (0, 2), "/": (0,3),
            '4': (1, 0), '5': (1,1), '6': (1,2), '*': (1,3),
            '1': (2,0), '2': (2,1), '3': (2,2), '-': (2,3),
            '0': (3, 0), 'C': (3,1), '=': (3,2), '+' :(3,3)
        }

        for texto, posicion in botones.items():
            boton = QPushButton(texto)
            boton.setStyleSheet("font-size: 18px;")
            boton.clicked.connect(self.manejar_click)
            self.grid_layout.addWidget(boton, *posicion)

    def manejar_click(self):
        # Coger el boton que esta mandando el click
        boton = self.sender()
        texto = boton.text()

        if texto == 'C':
            self.pantalla.clear()
        elif texto == '=':
            try:
                resultado = eval(self.pantalla.text())
                self.pantalla.setText(str(resultado))
            except Exception:
                self.pantalla.setText("Error")
        else:
            self.pantalla.setText(self.pantalla.text() + texto)


# El modulo principal que es lo ejecuta el archivo cuando le damos al play
if __name__ == "__main__":
    app = QApplication()
    interfaz = Calculadora()
    interfaz.show()
    app.exec()