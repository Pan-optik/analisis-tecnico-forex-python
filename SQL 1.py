import sqlite3

# Conectar (Crear el archivo si no existe)
ruta = r"C:\Users\HOLA\Curso Python Forex\forex.db"
conexion = sqlite3.connect(ruta)
cursor = conexion.cursor()

# Crear una tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS precios (
    fecha TEXT,
    precio REAL,
    señal TEXT
)
""")

conexion.commit()
print("Tabla creada")
