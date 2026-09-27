import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

datos = yf.download("EURUSD=X", period="180d", interval="1d")
precios = datos["Close"].squeeze()

# SMA 5 (Corto plazo)
sma_5 = precios.rolling(window=5).mean()

# Bandas de Bollinger (Basada en SMA 20)
sma_20 = precios.rolling(window=20).mean()
std_20 = precios.rolling(window=20).std()
banda_superior = sma_20 + (2 * std_20)
banda_inferior = sma_20 - (2 * std_20)

# Regresion lineal (Tendencia general)
x = np.arange(len(precios))
y = precios.values
pendiente, interseccion = np.polyfit(x, y, 1)
linea_tendencia = pendiente * x + interseccion

# Grafico combinado
plt.figure(figsize=(12, 7))
plt.plot(precios.index, precios.values, label="Precio de cierre", color="black", linewidth=1)
plt.plot(precios.index, sma_5, label="SMA 5", color="blue")
plt.plot(precios.index, banda_superior, label="Banda superior", color="green", linestyle="--")
plt.plot(precios.index, banda_inferior, label="Banda inferior", color="red", linestyle="--")
plt.plot(precios.index, linea_tendencia, label="Tendencia (regresion)", color="orange", linewidth=2)
plt.fill_between(precios.index, banda_inferior, banda_superior, alpha=0.1, color="gray")

plt.title("EUR/USD - Precio, SMA 5, Bollinger y Tendencia")
plt.xlabel("Fecha")
plt.ylabel("Precio")
plt.legend()

plt.show()