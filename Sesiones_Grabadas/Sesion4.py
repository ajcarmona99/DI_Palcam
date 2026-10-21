import PySide6.QtCore
from PySide6.QtGui import QAction, QKeySequence, QIcon
from PySide6.QtWidgets import QMainWindow, QApplication, QMenuBar, QWidget, QMenu, QMessageBox, QToolBar


# Siempre que queramos una interfaz usable con alguno de los contenidos de la sesion 4
# necesitamos que herede de QMainWindow.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sesion 4 Grabada")
        # Establecer aqui una geometria
        self.setGeometry(100, 100, 600, 400)

        ## CREAR UN WIDGET CENTRAL COMO LAYOUT PRINCIPAL
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        ## MENU PRINCIPAL
        menu_bar = QMenuBar()
        self.setMenuBar(menu_bar)

        ## AÑADIMOS OPCIONES DEL MENU
        file_menu = QMenu("Archivo")
        edit_menu = QMenu("Editar")
        menu_bar.addMenu(file_menu)
        menu_bar.addMenu(edit_menu)

        ## SI QUEREMOS DIFERENTES ACCIONES DENTRO DE UN MENU DESPLEGABLE
        new_action = QAction("Nuevo", self)
        open_action = QAction("Abrir", self)
        save_action = QAction("Guardar", self)

        ## AÑADIMOS EVENTOS A LO QUE SON LOS DESPLEGABLES DEL MENU
        new_action.triggered.connect(lambda : self.show_info("Nuevo seleccionado"))
        open_action.triggered.connect(lambda : self.show_info("Abrir seleccionado"))
        save_action.triggered.connect(lambda : self.show_info("Guardar seleccionado"))

        ## AÑADIMOS ATAJO TECLADO
        new_action.setShortcut(QKeySequence("Ctrl+N"))
        open_action.setShortcut(QKeySequence("Ctrl+A"))
        save_action.setShortcut(QKeySequence("Ctrl+S"))

        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)

        ## BARRA DE HERRAMIENTAS
        toolbar = QToolBar("Barra de herramientas", self)
        self.addToolBar(toolbar)
        # Añadir un boton dentro de la barra de herramientas
        toolbar_action = QAction(QIcon.fromTheme("help-browser"), "Mostrar mensaje", self)
        # Añadir el metodo de mostrar la emergente
        toolbar_action.triggered.connect(lambda : self.show_info("Has pulsado el boton de la barra de herramientas"))
        # Añadir un atajo de teclado
        toolbar_action.setShortcut(QKeySequence("Ctrl+M"))
        toolbar.addAction(toolbar_action)

        ## MENU CONTEXTUAL
        # (este menu contextual el que va a dispararlo es cuando se hace click derecho)
        self.setContextMenuPolicy(PySide6.QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)

    # Este metodo es el que va hacer mostrar dentro de la interfaz
    # un mensaje emergente
    def show_info(self, message):
        QMessageBox.information(self, "Mensaje", message)

    # Este metodo siempre te va a servir para mostrar un menu contextual
    # y aqui es donde se le indica siempre la posicion desde donde quieres que aparezca este menú
    def show_context_menu(self, position):
        # Creo el menu contextual
        context_menu = QMenu()
        # Aqui creo el interior de lo que es el menu contextual
        context_action = QAction("Accion contextual", self)
        context_menu.addAction(context_action)

        # Para que muestre el mensaje emergente
        context_action.triggered.connect(lambda : self.show_info("Has pulsado el menu contextual"))

        # Añadir un atajo de teclado
        context_action.setShortcut(QKeySequence("Ctrl+X"))

        # Para que aparezca en la posicion que te paso como parametro
        context_menu.exec(self.mapToGlobal(position))

if __name__ == "__main__":
    app = QApplication()
    ventana = MainWindow()
    ventana.show()
    app.exec()