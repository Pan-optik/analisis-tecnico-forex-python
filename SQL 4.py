import yfinance as yf
import sqlite3
import pandas as pd

datos = yf.download("EURUSD=X", period="30d", interval="1d")
datos = datos["Close"].squeeze()

soporte = datos.min()
resistencia = datos.max()

# Clsificar cada precio
senal = []
for precio in datos:
    if precio >= resistencia:
        senal.append("Ruptura alcista")
    elif precio <= soporte:
        senal.append("Ruptura bajista")
    else:
        senal.append("En rango")

tabla = pd.DataFrame({"precio": datos.values, "señal": senal}, index=datos.index)

ruta = r"C:\Users\HOLA\Curso Python Forex\forex.db"
conexion = sqlite3.connect(ruta)
tabla.to_sql("precios_con_señal", conexion, if_exists="replace")
conexion.commit()

# Mostar todo el contenido de la tabla
print("\nParte 1")
cursor = conexion.cursor()
cursor.execute("""
SELECT *
FROM precios_con_señal
""")
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)

# Contar cuantos dias hubo de cada señal
print("\nParte 2")
cursor = conexion.cursor()
cursor.execute("""
SELECT señal, COUNT(*)
FROM precios_con_señal
GROUP BY señal
""")
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)

# Combinando con otras agregaciones
print("\nParte 3")
cursor.execute("""
SELECT señal, COUNT(*), AVG(precio)
FROM precios_con_señal
GROUP BY señal
""")
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)