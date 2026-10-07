
from PySide6.QtWidgets import QMainWindow, QApplication


# Heredar de una clase lo que significa es que se otorga los atributos y los métodos de la clase padre
class Interfaz(QMainWindow):
    # Constructor de la clase
    def __init__(self):
        # Constructor de la clase padre - QMainWindow
        super().__init__()
        # Ponerle un título a la cabecera de la interfaz
        self.setWindowTitle("Primera interfaz")

if __name__ == "__main__":
    # Creo una instanciade una aplicación
    app = QApplication([])
    # Creo una instancia de la interfaz personalizada
    interfaz = Interfaz()
    # Muestro la interfaz
    interfaz.show()
    # El programa se mantiene en ejecución hasta que se cierre la interfaz inicializada
    app.exec()