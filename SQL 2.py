import yfinance as yf
import sqlite3

# Descargar datos de YF
datos = yf.download("EURUSD=X", period="30d", interval="1d")
datos = datos["Close"].squeeze()

# Conectar a base de datos
ruta = r"C:\Users\HOLA\Curso Python Forex\forex.db"
conexion = sqlite3.connect(ruta)

# Guardar el DataFrame como tabla SQL
datos.to_frame(name="precio").to_sql("precios", conexion, if_exists="replace")

conexion.commit()

cursor = conexion.cursor()
cursor.execute("SELECT * FROM precios")
resultados = cursor.fetchall()

for fila in resultados:
    print(fila)

cursor.execute("SELECT * FROM precios WHERE precio > 1.16")
resultados = cursor.fetchall()

print("Precio mayor que 1.16")

for fila in resultados:
    print(fila)