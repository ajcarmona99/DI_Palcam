import sqlite3

from PySide6.QtWidgets import QApplication

from database import conectar

# Esta funcion me sirve para registrar en el interior de la base de datos a la
# tabla que quiero
def registrar(id, usuario, password):

    try:
        # Primero me conecto a la base de datos que he creado anteriormente
        conexion = conectar()

        # Creo un cursor que me va a permitir realizar la consulta SQL
        cursor = conexion.cursor()

        # Ahora quiero que haga una consulta
        cursor.execute(
            "INSERT INTO usuarios (id, usuario, password) VALUES (?, ?, ?)",
            (id, usuario, password)
        )

        # Guardo los cambios
        conexion.commit()

        # Cierro la conexion
        conexion.close()

        return True
    except sqlite3.IntegrityError:
        return False

## Esta funcion lo que hace es devolverme el valor del id del usuario con
## el nombre y la contraseña que yo le paso por argumentos
def login(usuario, password):

    # Conexion con la base de datos
    conexion = conectar()

    # Creo el cursor para poder hacer la consulta
    cursor = conexion.cursor()

    # Ejecuto la consulta
    cursor.execute(
        "SELECT id FROM usuarios WHERE usuario=? AND password=?",
        (usuario, password)
    )

    # Ahora tomo la fila donde coincide este usuario y esta contraseña
    row = cursor.fetchone()
    conexion.close()
    return row[0] if row else None
