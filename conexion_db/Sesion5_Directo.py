from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
from auth import actualizar

class VentanaActualizar(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Actualizar usuario")

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.input_id = QLineEdit()
        self.input_id.setPlaceholderText("ID del usuario que quieres actualizar")
        self.input_nombre = QLineEdit()
        self.input_nombre.setPlaceholderText("Nuevo nombre de usuario")
        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("Nueva contraseña")
        self.input_password.setEchoMode(QLineEdit.Password)
        btn_actualizar = QPushButton("Actualizar")
        btn_actualizar.clicked.connect(self.actualizar_usuario)

        layout.addWidget(QLabel("ACTUALIZAR USUARIO"))
        layout.addWidget(self.input_id)
        layout.addWidget(self.input_nombre)
        layout.addWidget(self.input_password)
        layout.addWidget(btn_actualizar)

    def actualizar_usuario(self):
        try:
            id_usuario = int(self.input_id.text())
        except ValueError:
            QMessageBox.warning(
                self, "ID incorrecto", "El ID debe de ser un numero entero"
            )
            return

        usuario = self.input_nombre.text().strip()
        password = self.input_password.text().strip()

        if not usuario or not password:
            QMessageBox.warning(
                self, "Campos vacios", "Introducir el nombre y la contraseña"
            )
            return


        if actualizar(id_usuario, usuario, password):
            QMessageBox.information(self, "OK", "Usuario actualizado")
            self.input_password.clear()
        else:
            QMessageBox.warning(self, "Usuario no encontrado", "No existe ningun usuario con ese ID")



if __name__ == "__main__":
    app = QApplication()
    interfaz = VentanaActualizar()
    interfaz.show()
    app.exec()