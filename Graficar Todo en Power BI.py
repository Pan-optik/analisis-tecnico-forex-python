import yfinance as yf
import numpy as np
import pandas as pd
import sqlite3

datos = yf.download("EURUSD=X", period="180d", interval="1d")
precios = datos["Close"].squeeze()

sma_5 = precios.rolling(window=5).mean()
sma_20 = precios.rolling(window=20).mean()
std_20 = precios.rolling(window=20).std()
banda_superior = sma_20 + (2 * std_20)
banda_inferior = sma_20 - (2 * std_20)

x = np.arange(len(precios))
pendiente, interseccion = np.polyfit(x, precios.values, 1)
tendencia = pendiente * x + interseccion

tabla = pd.DataFrame({
    "precio": precios.values,
    "sma_5": sma_5.values,
    "banda_superior": banda_superior.values,
    "banda_inferior": banda_inferior.values,
    "tendencia": tendencia
}, index=precios.index)

ruta = r"C:\Users\HOLA\Curso Python Forex\IndiCompletos.db"
conexion = sqlite3.connect(ruta)
tabla.to_sql("Indicadores completos", conexion, if_exists="replace")
conexion.commit()
print("Tabla de indicadores creada")