import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

datos = yf.download("EURUSD=X", period="30d", interval="1d")
precios = datos["Close"].squeeze()

# Convertir fechas a numeros (0, 1, 2...) para regresion
x = np.arange(len(precios))
y = precios.values

# Calcular pendiente e interseccion
pendiente, interseccion = np.polyfit(x, y, 1)

print(f"Pendiente: {pendiente:.6f}")
print(f"Interseccion: {interseccion:.4f}")

# Graficar linea de tendencia sobre el precio
linea_tendencia = pendiente * x + interseccion

plt.plot(precios.index, y, label="Precio de cierre")
plt.plot(precios.index, linea_tendencia, label="Linea de tendencia", color="red", linestyle="--")
plt.title("EUR/USD - Tendencia (Regresion Lineal)")
plt.xlabel("Fecha")
plt.ylabel("Precio")
plt.legend()

plt.show()