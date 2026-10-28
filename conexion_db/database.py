import sqlite3

DB_NAME = "usuarios.db"

# Con esta funcion que hemos creado, se crea tanto la base de datos como se conecta
# Si hay una base de datos con este nombre se conecta directamente.
# Si no la hay, se crea automáticamente.
def conectar():
    conexion = sqlite3.connect(DB_NAME)
    return conexion

# Esta función es la que va hacer crear las tablas de mi usuario
def crear_tablas():
    # Primero conectar a la base de datos
    conexion = conectar()

    # Preparo un cursor sobre el que voy a realizar la consulta
    cursor = conexion.cursor()

    # Escribo en sintaxis de tipo SQL
    cursor.execute("""
    CREATE TABLE usuarios(
        id PRIMARY KEY,
        usuario TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    # Tenemos que guardar los cambios
    conexion.commit()

    # Cerramos conexion
    conexion.close()


