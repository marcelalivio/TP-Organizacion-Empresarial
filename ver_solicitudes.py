import sqlite3

conexion = sqlite3.connect("equipamiento.db")
cursor = conexion.cursor()

cursor.execute("""
SELECT *
FROM solicitudes
""")

solicitudes = cursor.fetchall()

for solicitud in solicitudes:
    print(solicitud)

conexion.close()