from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout


class Contador(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Contador")

        # Contruyo el layout
        layout = QVBoxLayout()




        # A esta interfaz le establezco este layout
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    contador = Contador()
    contador.show()
    app.exec()