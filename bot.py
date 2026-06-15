import sqlite3

print("*** Bienvenido al Sistema de Solicitud de Equipamiento ***")

# Conexión a SQLite
conexion = sqlite3.connect("equipamiento.db")
cursor = conexion.cursor()

legajo = input("Por favor ingrese su número de legajo: ")
cursor.execute(
    "SELECT nombre FROM empleados WHERE legajo = ?",
    (legajo,)
)
empleado = cursor.fetchone()

if empleado:

    print(f"\nBienvenido, {empleado[0]}!")

    print("\n¿Qué tipo de equipamiento desea solicitar?")
    print("1. Laptop")
    print("2. Monitor")
    print("3. Teclado")
    print("4. Ratón")
    print("5. Auriculares")

    opcion = input("Ingrese el número correspondiente a su solicitud: ")

    equipos = {
        "1": "Laptop",
        "2": "Monitor",
        "3": "Teclado",
        "4": "Ratón",
        "5": "Auriculares"
    }

    if opcion not in equipos:
        print("Opción no válida.")
        conexion.close()
        exit()

    equipo = equipos[opcion]

    print(f"\nHas solicitado: {equipo}")
    print("Consultando stock...")

    cursor.execute(
        "SELECT cantidad FROM stock WHERE equipo = ?",
        (equipo,)
    )

    resultado = cursor.fetchone()

    if resultado and resultado[0] > 0:

        print("\nSolicitud aprobada.")
        print("El área de IT se pondrá en contacto contigo.")

        cursor.execute("""
            INSERT INTO solicitudes
            (legajo, equipo, estado)
            VALUES (?, ?, ?)
        """, (legajo, equipo, "APROBADA"))

    else:

        print("\nNo hay stock disponible.")
        print("La solicitud fue registrada como pendiente.")

        cursor.execute("""
            INSERT INTO solicitudes
            (legajo, equipo, estado)
            VALUES (?, ?, ?)
        """, (legajo, equipo, "PENDIENTE"))

    conexion.commit()

else:
    print("\nNúmero de legajo no reconocido.")

conexion.close()