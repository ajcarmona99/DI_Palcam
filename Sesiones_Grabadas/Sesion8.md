# Introduccion

En las clase anteriores hemos aprendido a crear interfaces con PySide6, conectar
botones con funciones y separar un poco la logica de la interfaz.

Hasta ahora, cada vez que queriamos añadir elementos a una ventana,
creabamos los componentes dentro de la misma.

Pero imaginad que necesitamos el mismo conjunto de elemento en cinco
ventanas distintas ¿Tenemos que escribir el mismo código cinco veces?

Utilizando POO.

# Contenidos

1) Ejemplo básico.
2) Contador.
3) Control de volumen.
4) Indicador de bateria.
5) Ejercicio.


# Control de volumen

Ahora lo que se va a introducir a partir de este ejemplo es la parte más importante de la clase: crear
nuestras propias señales dentro de un componente personalizados.

Hasta ahora hemos utilizado señales de PySide6 que ya nos proporciona, como clicked o si quereis
verlo el ValueChanged(cuando cambio el valor de una linea).

Cuando el usuario mueve el slider suceder tres cosas:

* Primero, el slider emite su señal de ValueChanged.
* Segundo, nuestro componente recibe el valor y actualiza su etiqueta.
* Y tercero, el componente emite su propia señal volumenCambiado.

De esta forma, el componente recibe una señal interna y comunica hacia fuera lo que ha sucedido.

# Indicador de bateria

Vamos a convertir la representación de un componente visual reutilizable, en una reprensetación
de una bateria.

# Ejercicio para casa

Crea un boton personalizado, que le puedas pasar el texto y el color del mismo boton.

Y haz que si pulsas ese boton se añada un popup avisando al usuario que ese boton ha sido pulsado.

Intenta hacerlo en archivos diferentes, es decir, no lo que estamos haciendo hasta ahora,
si no con importación de archivos para ver que no tienen porque estar en el mismo proyecto.

