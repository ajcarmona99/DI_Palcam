from msilib.schema import Shortcut

from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import QLineEdit, QMainWindow, QWidget, QVBoxLayout, QLabel, QApplication, QMenu


class EntradaConMenu(QLineEdit):
    """Entrada personalizada con menú contextual y atajos"""
    def __init__(self):
        # Inicializar la clase del QLineEdit
        super().__init__()

        # Texto orientativo que este desaparece al escribir
        self.setPlaceholderText("Escribe aquí y pulsa el botón derecho...")

        # Nombre que va a ser utilizado por las herramientas de accesibilidad
        self.setAccessibleName("Texto del usuario")

        # Altura minima de la entrada
        self.setMinimumHeight(38)

    def crear_accion(self, nombre, atajo, funcion):
        # Asociar la accion a esta entrada
        accion = QAction(nombre, self)

        # Convierto el texto del atajo a una secuencia
        accion.setShortcut(QKeySequence(atajo))

        accion.triggered.connect(funcion)

        self.addAction(accion)
        return accion

    def keyPressEvent(self, evento):
        combinacion = QKeySequence(evento.keyCombination())

        acciones = (
            self.accion_borrar,
            self.accion_copiar,
            self.accion_pegar,
            self.accion_limpiar
        )

        for accion in acciones:
            if combinacion == accion.shortcut():
                accion.trigger()

                evento.accept()
                return

        super().keyPressEvent(evento)

    def copiar_texto(self):
        if self.hasSelectedText():
            texto = self.selectedText()
        else:
            texto = self.text()


        if texto:
            QApplication.clipboard().setText(texto)

    def mostrar_menu(self, posicion):
        menu = QMenu(self)

        menu.addAction((self.accion_borrar))
        menu.addAction(self.accion_copiar)
        menu.addAction(self.accion_pegar)

        menu.exec(self.mapToGlobal(posicion))




class VentanaPrincipal(QMainWindow):
    """Ventana principal de la aplicación"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Entrada con menu")
        self.resize(640, 250)

        contenedor = QWidget(self)
        self.setCentralWidget(contenedor)

        layout = QVBoxLayout(contenedor)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(12)

        self.entrada = EntradaConMenu()

        etiqueta = QLabel("&Texto del usuario:")

        etiqueta.setBuddy(self.entrada)

        layout.addWidget(etiqueta)
        layout.addWidget(self.entrada)

if __name__ == "__main__":
    app = QApplication()
    interfaz = VentanaPrincipal()
    interfaz.show()
    app.exec()