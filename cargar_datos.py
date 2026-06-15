import sqlite3

conexion = sqlite3.connect("equipamiento.db")
cursor = conexion.cursor()

empleados = [
    (1, "Marcela"),
    (2, "Juan"),
    (3, "Ana"),
    (4, "Pedro"),
    (5, "Lucía"),
    (6, "Carlos"),
    (7, "María"),
    (8, "Sofía"),
    (9, "Diego"),
    (10, "Laura")
]

cursor.executemany(
    "INSERT INTO empleados (legajo, nombre) VALUES (?, ?)",
    empleados
)

stock = [
    ("Laptop", 5),
    ("Monitor", 3),
    ("Teclado", 8),
    ("Ratón", 0),
    ("Auriculares", 0)
]

cursor.executemany(
    "INSERT INTO stock (equipo, cantidad) VALUES (?, ?)",
    stock
)

conexion.commit()

print("Datos cargados correctamente")

conexion.close()