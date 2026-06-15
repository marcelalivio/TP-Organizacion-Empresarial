import sqlite3

conexion = sqlite3.connect("equipamiento.db")

cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS empleados(
    legajo INTEGER PRIMARY KEY,
    nombre TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS stock(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    equipo TEXT,
    cantidad INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS solicitudes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    legajo INTEGER,
    equipo TEXT,
    estado TEXT
)
""")

conexion.commit()

print("Base de datos creada correctamente")

conexion.close()
