from PySide6.QtWidgets import QWidget, QApplication, QGridLayout


class TableroAjedrez(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tablero de ajedrez")
        # Un tablero es un cuadrado por tanto el ancho y el alto miden lo mismo
        self.setFixedSize(480, 480)

        # Esta claro que es un layout de rejillas
        grid = QGridLayout(self) #(self) en el layout es como poner self.setLayout(grid)

        # Si no quiero que haya espacios entre casillas
        grid.setSpacing(0)

        # Ahora elimino los margenes
        grid.setContentsMargins(0, 0, 0, 0)

        # Como necesito 8 filas y 8 columnas introduzco un bloque anidado
        for fila in range(8):
            for columna in range(8):
                # Fila par columna par negro
                # Fila impar columna impar negro
                color = "white" if (fila + columna) % 2 == 0 else "black"
                # Para crear la casilla utilizo el Widget general
                casilla = QWidget()
                casilla.setStyleSheet(f"background-color: {color}")
                # Añadir cada casilla poco a poco en el bucle al grid
                grid.addWidget(casilla, fila, columna)

        # Establezco un indice
        for indice in range(8):
            grid.setRowStretch(indice, 1)
            grid.setColumnStretch(indice, 1)
if __name__ == "__main__":
    app = QApplication()
    tablero = TableroAjedrez()
    tablero.show()
    app.exec()