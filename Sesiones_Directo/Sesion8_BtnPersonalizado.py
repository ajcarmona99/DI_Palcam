from PySide6.QtGui import QColor
from PySide6.QtWidgets import QPushButton, QApplication


# Aqui estamos diciendo que la clase padre es un boton
class BotonPersonalizado(QPushButton):
    def __init__(self, texto : str, color : str):
        # Aqui establezco el texto el boton
        super().__init__(texto)

        # Ahora tomo el color que tambien se lo estoy pasando por argumento
        fondo = QColor(color)

        # Le puedo pasar un color que no es represantable
        if not fondo.isValid():
            # Lanzar una excepcion para decirme que le estoy pasando un color no valido
            raise ValueError(f"Color inválido: {color}")

        self.setStyleSheet(f"""
            QPushButton{{
                background-color: {fondo.name()};
                color: white;
                border: 1px;
                border-radius: 8px;
                padding: 10px 18px;
            }}
        """)

