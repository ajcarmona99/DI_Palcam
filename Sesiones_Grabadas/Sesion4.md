# Objetivo

Vamos a comenzar a realizar lo que son interfaces usables.

# ¿Que es usabilidad?

Hacer que la interfaz sea capaz de utilizarla todas las personas.

# Contenido

1. Menu superiores.
2. Menu contextuales.
3. Mensajes emergentes. (Vienen de la libreria QMessageBox)
4. Barra de herramientas (QToolBar)

Si queremos crear lo que viene siendo los componentes principales del menú tenemos
que crearlo a partir de lo demainado QMenu.
La componente que alberga a todos los QMenu.

QMenuBar - QMenu - QAction.

Atajo teclado -> QKeySequence

# Para crear un menu contextual

1. La funcion que determina donde va a aparecer dicho menu.
2. QMenu y dentro unos QAction que son los que van a definir la funcionalidad
del menu.
3. Tienes que establecerle la politica comun de un menu contextual.

(Este hace que tu menu sepa que tiene que salir cuando haces click derecho en la interfaz)

# Ejercicio para casa

Quiero que incorpores una interfaz que tenga:

* Una entrada de texto para el usuario.
* Funciones que debe de tener el menu contextual:

Borrar lo de la entrada.
Copiar lo de la entrada.
Pegar lo de la entrada.
Limpiar lo de la entrada.

* Establecer a todo lo que es un atajo de teclado.