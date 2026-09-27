import sqlite3

ruta = r"C:\Users\HOLA\Curso Python Forex\forex.db"
conexion = sqlite3.connect(ruta)

cursor = conexion.cursor()
cursor.execute("SELECT * FROM precios ORDER BY precio DESC LIMIT 5")
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)

cursor.execute("SELECT AVG(precio), MAX(precio), MIN(precio), COUNT(*) FROM precios")
resultado= cursor.fetchall()
print(resultado)