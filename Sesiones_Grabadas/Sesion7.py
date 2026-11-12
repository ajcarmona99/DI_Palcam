from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QHBoxLayout, QLineEdit, QVBoxLayout, QLabel, \
    QTableView, QTableWidget, QPushButton, QMessageBox, QTableWidgetItem


class Ejemplo1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(800, 400)

        # Utilizo un loader que es un objeto que carga archivos de tipo ui
        loader = QUiLoader()
        archivo = QFile("../ui/InterfazSesion7Ejemplo1.ui")

        # Le digo que la interfaz es ese archivo
        self.ui = loader.load(archivo)
        archivo.close()

        # Establezco esa interfaz como central Widget
        self.setCentralWidget(self.ui)

class GestorProductos(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de productos")
        self.setMinimumSize(500, 400)

        # Establecemos aqui nuestro layout principal
        self.layout_principal = QVBoxLayout()
        self.setLayout(self.layout_principal)

        # Llamamos al método que hace que se incorporen los formularios a la interfaz
        self.crear_formularios()

        # Llamamos al método que hace que incorpore la tabla a la interfaz
        self.crear_tabla()

        # Añado los botones que van a permitir añadir a la tabla
        self.crear_botones()

    # Metodo que va hacer crear los formularios
    def crear_formularios(self):
        # Primero se crea el layout que va a representar los formularios
        # y se añaden las componentes al mismo
        layout_form = QHBoxLayout()

        self.input_nombre = QLineEdit()
        self.input_precio = QLineEdit()

        layout_form.addWidget(QLabel("Nombre:"))
        layout_form.addWidget(self.input_nombre)
        layout_form.addWidget(QLabel("Precio:"))
        layout_form.addWidget(self.input_precio)

        # Una vez que tengamos creado el layout del formulario se lo añadimos al layout principal
        self.layout_principal.addLayout(layout_form)

    def crear_tabla(self):
        # Este objeto es el que representa una tabla en PySide6
        self.tabla = QTableWidget()

        # Establezco la columnas
        self.tabla.setColumnCount(2)

        # Establezco el nombre de las columnas
        self.tabla.setHorizontalHeaderLabels(["Nombre", "Precio"])

        # Que en la tabla se pueda seleccionar una fila de manera unica que me va permitir eliminar la que quiera
        self.tabla.setSelectionBehavior(QTableWidget.SelectRows)
        self.tabla.setSelectionMode(QTableWidget.SingleSelection)

        # Añadir la tabla a mi layout
        self.layout_principal.addWidget(self.tabla)

    def crear_botones(self):
        # Primero creo el layout donde se encuentran los botones
        layout_botones = QHBoxLayout()
        btn_agregar = QPushButton("Añadir producto")
        # Añado el metodo que hace agregar el producto
        btn_agregar.clicked.connect(self.agregar_producto)
        btn_eliminar = QPushButton("Eliminar producto")
        btn_eliminar.clicked.connect(self.eliminar_producto)

        # Añadimos a ese layout esos botones
        layout_botones.addWidget(btn_agregar)
        layout_botones.addWidget(btn_eliminar)

        # Añado ese layout al layout principal
        self.layout_principal.addLayout(layout_botones)

    def agregar_producto(self):
        # Primero tomo el nombre y el precio de los inputs
        nombre = self.input_nombre.text().strip()
        precio = self.input_precio.text().strip()

        # Si no hay un nombre o in precio que salte un mensaje de aviso
        # Si introduzco en el precio algo que no sea un numero que salte tambien un aviso
        if not nombre or not precio:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios")
            return

        try:
            float(precio)
        except ValueError:
            QMessageBox.warning(self, "Error", "El precio debe de ser un numero")

        # Tenemos que añadir la fila que queramos
        fila = self.tabla.rowCount()
        self.tabla.insertRow(fila)

        # Establecemos las propiedades de esa fila
        self.tabla.setItem(fila, 0, QTableWidgetItem(nombre))
        self.tabla.setItem(fila, 1, QTableWidgetItem(precio))

        # Una vez que se añada que elimine el texto de los campos
        self.input_precio.clear()
        self.input_nombre.clear()

    def eliminar_producto(self):
        # Primero eligo la fila y posteriormente la elimino de la tabla
        fila_seleccionada = self.tabla.currentRow()
        if fila_seleccionada == -1:
            QMessageBox.warning(self, "Aviso", "Selecciona un producto para eliminar")
            return

        # Elimino la fila seleccionada
        self.tabla.removeRow(fila_seleccionada)

class Ejemplo3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(800, 400)

        # Utilizo un loader que es un objeto que carga archivos de tipo ui
        loader = QUiLoader()
        archivo = QFile("../ui/InterfazSesion7Ejemplo3.ui")

        # Le digo que la interfaz es ese archivo
        self.ui = loader.load(archivo)
        archivo.close()

        # Establezco esa interfaz como central Widget
        self.setCentralWidget(self.ui)
        # Establezco el metodo de sumar a mi btn
        self.ui.btn.clicked.connect(self.sumar)

    def sumar(self):
        # TENGO QUE RECORDAR MUY BIEN QUE IDENTIFICADORES HE PUESTO A LA HORA DE CREAR LA INTERFAZ
        # A PARTIR DEL DESIGNER
        try:
            num1 = float(self.ui.num1.text())
            num2 = float(self.ui.num2.text())
            QMessageBox.information(self, "Resultado", f"El resultado es: {str(num1 + num2)}")
        except ValueError:
            QMessageBox.warning(self, "Error", "Los dos inputs tienen que ser numeros")


if __name__ == "__main__":
    app = QApplication()
    ventana = Ejemplo3()
    ventana.show()
    app.exec()