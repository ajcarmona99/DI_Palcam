import csv

filas = [
    ["Nombre", "Mes", "Precio"],
    ["Antonio", "Enero", 3000],
    ["Marina", "Febrero", 7500],
    ["Ruth", "Febrero", 10000]
]

with open("Sesion9.csv", "w", newline="", encoding="utf-8-sig") as archivo:
    escritor = csv.writer(archivo, delimiter=";")
    escritor.writerows(filas)