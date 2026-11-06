import requests
from PySide6 import QtGui
from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QApplication, QPushButton
from threads import ObtenerImagenesThread
from database import conectar

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conexion con API")

        # Layout que es de rejilla porque me interesa que esten las imagenes
        # divididas en dos filas
        self.layout = QGridLayout(self) # Recordar que con el (self) en el layout es igual que un self.setLayout
        self.label = QLabel("Cargando imágenes...")
        self.layout.addWidget(self.label)

        # A partir del hilo definido anteriormente pinto las imagenes
        self.thread = ObtenerImagenesThread()

        # Es lo mismo que decirlo que a mostrar le paso el argumento de las urls
        self.thread.imagenes_obtenidas.connect(self.mostrar)

        # Inicializo el hilo
        self.thread.start()

    # Este metodo lo que haces es a partir de un array de URLs las pinta en las interfaces
    def mostrar(self, urls):
        self.label.setText("")

        # Para cada posición y cada url que conforme el array
        for i, url in enumerate(urls):
            # Hago la consulta HTTP, a pattir de la URL de la imagen y una vez que la tengo tomo su contenido
            img = requests.get(url).content

            # Pintamos la imagen
            pix = QtGui.QPixmap()
            pix.loadFromData(img)

            # Ahora lo muestro en la interfaz
            lbl = QLabel()

            # Longitud de cuadrado de 180 por 180
            lbl.setPixmap(pix.scaled(180, 180))
            self.layout.addWidget(lbl, i // 3 + 1, (i%3) * 2)

            # Voy a poner un boton para que el usuario puedes le permita la interfaz
            # poder marca si es de sus favoritos o no
            btn = QPushButton("☆")
            self.layout.addWidget(btn, i // 3 + 1 , (i % 3) * 2 + 1)
            btn.clicked.connect(lambda c, u=url, b = btn: self.toggle(u, c, b))

    # Con esto definimos la funcion que va a hacer que  se encuentre en la base de datos
    def toggle(self, url, checked, btn):
        # Primeramente me conecto a la base de datos que ya tenia creada
        conexion = conectar()

        # Creo un cursor que va a ser quien me permita alimentar la base de datos
        # e insertar
        cursor = conexion.cursor()

        if checked:
            # Ahora inserto en el interior de la base de datos
            cursor.execute(
                "INSERT INTO favoritos (url) VALUES (?)",
                (url)
            )

            # El boton que hemos pulsado que aparezca ya coloreado
            btn.setText("★")

        else:

            # Si desmarco el boton quiero que elimine esta imagen de mi tabla de favoritos
            # Ahora tengo que hacer un DELETE de la base de datos
            cursor.execute(
                "DELETE FROM favoritos WHERE url = ?",
                (url)
            )
            btn.setText("☆")







if __name__ == "__main__":
    app = QApplication()
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
