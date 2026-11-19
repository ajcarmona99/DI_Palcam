from PySide6.QtCore import Signal, Qt, Slot
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QApplication, QSlider, QProgressBar


class Ventana(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        label = QLabel("Contador: 0")
        boton = QPushButton("Sumar")

        layout.addWidget(label)
        layout.addWidget(boton)

# En este codigo no tenemos un contador de verdad. Vamos a transformar estos elemento en un componente
# personalizado llamado ContadorWidget.
#
# La diferencia importancia entre lo que estabamos haciendo y lo que vamos a hacer es que esta componente,
# tendra sus propios widgets, su propio comportamiento y mas adelante sus propios señales.

class ContadorWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.contador = 0
        self.label = QLabel("Contador: 0")
        self.boton_sumar = QPushButton("Sumar")
        # Conecto el boton
        self.boton_sumar.clicked.connect(self.sumar)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.boton_sumar)

    # Añadiendo el metodo al hacer click al boton acabamos de encapsular el comportamiento del contador.
    # Si yo utilizo este contador en una ventana princiapl no necesita saber como se actualiza la etiqueta,
    # porque de eso se ocupa la componente
    # Añado un comportamiento al contador
    def sumar(self):
        self.contador +=1
        self.label.setText(f"Contador: {self.contador}")

class EjemploContador(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Componentes personalizados")
        # Como tengo un contador creado como componente personalizado puedo utilizarlo tantas veces como desee

        layout = QVBoxLayout(self)

        self.contador1 = ContadorWidget()
        self.contador2 = ContadorWidget()

        layout.addWidget(self.contador1)
        layout.addWidget(self.contador2)

# Fijaoos lo que se acaba de conseguir: tenemos dos contadores completamente independientes y no hemos duplicado
# el código de implementación. Por tanto es más fácil la busqueda de errores en el caso de problemas de implantación
# y ademmás si quieres realizar un cambio personalizado dentro de la propio componente solo debes de irte a
# la clase donde estes definiendo la mismo.

# Cada instancia (creacion de un objeto con esa clase) tiene su propio valor, sus botones y sus conexiones.
# Esto es una ventaja bastante considerable ua que puedes reutilizar una misma funcionalidad tantas veces como queramos.


# ¿Que pasa si la ventana principal necesita saber que el usuario ha cambiado de volumen?
# Podriamos hacer es acceder directamente al slider del componente, pero para eso haria que nuestra ventana dependiese demasiado como
# esta construido internamente.
# La solucion es que nuestro componente emita una señal propia.

class ControlVolumen(QWidget):

    # Esta señal es la que avisa a la interfaz princiapl de que el volumen que es la propiedad que me interesa
    # esta siendo cambiada
    volumenCambiado = Signal(int)

    def __init__(self):
        super().__init__()
        self.label = QLabel("Volumen: 50")

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.setValue(50)

        # Se avisa a la interfaz de que el slider esta cambiando de valor a traves de la señal que nos proporciona el PySide6 que es el de
        # valueChanged
        self.slider.valueChanged.connect(self.actualizar_volumen)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.slider)

    @Slot(int)
    def actualizar_volumen(self, valor):
        self.label.setText(f"Volumen: {valor}")
        self.volumenCambiado.emit(valor)

    # Quiero mejorar la componente. Imagino que otra ventana quiere establecer el volumen en 0.
    # No quieres escribir por ejemplo desde otro archivo slider.setValue(80), por para eso
    # o para añadir más funcionalides lo que hacemos es añadir más métodos

    def set_volumen(self, valor):
        self.label.setText(f"Volumen: {valor}")
        self.slider.setValue(valor)

    def get_volumen(self, valor):
        return self.slider.value()

class EjemploVolumen(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        volumen = ControlVolumen()
        volumen.set_volumen(80)
        layout.addWidget(volumen)

class IndicadorBateria(QWidget):
    def __init__(self, numero):
        super().__init__()

        self.label = QLabel(f"Batería: {numero}%")

        self.barra = QProgressBar()
        self.barra.setRange(0, 100)
        self.barra.setValue(numero)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.barra)

    # Con lo que tenemos hecho hasta el momento solo tenemos una equita y una barra de progreso.
    # Ahora vamos a darle un metodo publico para actualizarlo
    @Slot(int)
    def set_nivel(self, nivel):

        nivel = max(0, min(100, nivel))

        self.label.setText(f"Batería: {nivel}%")
        self.barra.setValue(nivel)

        # Este  metodo recibe un numero y actualiza los elementos visuales.
        # Limito el valor entre 0 y 100. Por si alguien intenta establecer un valor de 150, la componente en 100.
        # Añadimos un comportamiento visual.

        if nivel <= 20:
            color = "#dc554f"
        elif nivel <= 40:
            color = "#d99b29"
        else:
            color = "#399a70"

        # Establezco ese color a la barra
        self.setStyleSheet(f"""
        QProgressBar::chunk{{
            back-ground-color: {color}
        }}
        """)

if __name__ == "__main__":
    app = QApplication()
    interfaz = IndicadorBateria(10)
    interfaz.show()
    app.exec()