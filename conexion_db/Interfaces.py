from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
import sqlite3
from auth import registrar, login

class VentanaRegistro(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("REGISTRO")

        # Establezco un layout vertical
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Voy a crear todas las componentes que van a formar parte de nuestro layout
        label = QLabel("REGISTRO")
        self.input_id = QLineEdit()
        self.input_id.setPlaceholderText("ID del usuario")
        self.input_nombre = QLineEdit()
        self.input_nombre.setPlaceholderText("Nombre de usuario")
        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("Contraseña del usuario")
        self.input_password.setEchoMode(QLineEdit.Password)
        btn_registro = QPushButton("Registrar")
        btn_registro.clicked.connect(self.registrar)

        layout.addWidget(label)
        layout.addWidget(self.input_id)
        layout.addWidget(self.input_nombre)
        layout.addWidget(self.input_password)
        layout.addWidget(btn_registro)

    def registrar(self):
        try:
            # Si se cumple el registro
            if registrar(int(self.input_id.text()), self.input_nombre.text(), self.input_password.text()):
                QMessageBox.information(self, "OK", "Usuario creado")
            else:
                QMessageBox.warning(self, "Error", "Usuario existe")
        except ValueError:
            # Si el usuario introduce lo que es un id que no es un entero
            QMessageBox.warning(self, "Problema con el id", "El ID debe de ser un numero entero")

# Esta es la clase en la que se define la interfaz del login
class VentanaLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.input_nombre = QLineEdit()
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)
        btn_login = QPushButton("Iniciar sesion")
        btn_login.clicked.connect(self.logear)

        layout.addWidget(self.input_nombre)
        layout.addWidget(self.input_password)
        layout.addWidget(btn_login)

    # Este metodo es el que me permite comprobar en el interior de la base de datos si se encuentra o no el usuario
    def logear(self):

        # Tomo el id de la fila que estoy buscando
        id = login(self.input_nombre.text(), self.input_password.text())

        # Si el id no es vacio
        if id:
            QMessageBox.information(self, "Login", "Usuario logueado")
        else:
            QMessageBox.warning(self, "Error", "Ese usuario no se encuentra creado")

if __name__ == "__main__":
    app = QApplication()
    registro = VentanaLogin()
    registro.show()
    app.exec()