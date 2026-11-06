import requests
from PySide6.QtCore import QThread, Signal


class ObtenerImagenesThread(QThread):
    # Voy a tener una lista que va a obtener todos las URL de las imagenes
    imagenes_obtenidas = Signal(list)

    def run(self):
        try:
            r = requests.get("https://picsum.photos/v2/list?limit=6")

            # Esta solicitud espera a que termine la lectura de todas las imagenes
            r.raise_for_status()

            # Voy a tomar los campos de URL que son los que me interesan
            urls = [img["download_url"] for img in r.json()]

            # Retorno a partir de este hilo
            self.imagenes_obtenidas.emit(urls)
        except Exception as e:
            print("Error: e")
            self.imagenes_obtenidas.emit([])