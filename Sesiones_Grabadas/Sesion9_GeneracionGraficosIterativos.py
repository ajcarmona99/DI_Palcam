import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QMainWindow, QApplication, QComboBox, QVBoxLayout, QWidget, QPushButton, QMessageBox

fichero = "Sesion9.csv"
df = pd.read_csv(fichero)
IMG_BARRAS = Path("BARRAS.png")
IMG_PIE = Path("PIE.png")
HTML = Path("Sesion9.html")

def generar_grafico(df, mes):
    datos = df[df["Mes"] == mes]

    # GRAFICO DE BARRAS
    plt.figure()
    # Agrupar por nombre y precio, es decir va a salir el total de ventas en el mes que estoy filtrando
    datos.groupby("Nombre")["Precio"].sum().plot(kind="bar")
    plt.title(f"Ventas en {mes}")
    plt.ylabel("Importe")
    plt.tight_layout()
    plt.savefig(IMG_BARRAS)

    # GRAFICO DE SECTORES
    plt.figure()
    datos.groupby("Nombre")["Precio"].sum().plot(kind="pie")
    plt.title("Unidades vendidas")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(IMG_PIE)

def generar_html(df, mes):
    # Tranformo en texto html la tabla filtrada por el mes que le estoy pasando
    tabla_html = df[df["Mes"] == mes].to_html(index=False)
    # Llamo a la funcion que me genera los graficos
    generar_grafico(df, mes)
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Tabla filtrada por {mes}</title>
    </head>
    <body>
    <h1>Informe de ventas</h1>
    <h3>Ventas por vendedor</h3>
    <img src="{IMG_BARRAS.name}">
    <h3>Detalle de ventas</h3>
    <img src="{IMG_PIE.name}">
    <h3>Tabla</h3>
    {tabla_html}
    </body>
    </html>
    """

    # Al archivo anterior que he creado le introduzco de contenido el texto del html
    HTML.write_text(html, encoding="utf-8")

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        # Tengo que decirle con que datos voy a tratar
        self.df = df
        self.setWindowTitle("Informe de ventas")

        # Se pone la pantalla un poquito más grande para poder visualizar con comodidad todo el HTML
        self.resize(1200, 800)

        self.combo = QComboBox()
        # Al combo box le estoy añadiendo los meses de mis datos de manera unica
        self.combo.addItems((sorted(df["Mes"].unique())))
        # Se añade un boton que va a ser el que va a generar el informe
        self.btn = QPushButton("Actualizar informe")

        # Añado el metodo de actualizar al boton
        self.btn.clicked.connect(self.actualizar)

        # Un componente que permite dentro del PySide ser un visualizador de HTML
        self.web = QWebEngineView()


        layout = QVBoxLayout()
        contenedor = QWidget()

        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

        layout.addWidget(self.combo)
        layout.addWidget(self.btn)
        layout.addWidget(self.web)

    # Este metodo va a actualizar el informe con los graficos y ademas lo va a mostrar en la interfaz
    def actualizar(self):
        mes = self.combo.currentText()
        try:
            # Se intenta generar el HTML
            generar_html(self.df, mes)

            # Al visualizador web de la interfaz le indico la ruta en la que esta el HTML
            self.web.setUrl(QUrl.fromLocalFile(str(HTML.resolve())))

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

app = QApplication()
ventana = Ventana()
ventana.show()
app.exec()

