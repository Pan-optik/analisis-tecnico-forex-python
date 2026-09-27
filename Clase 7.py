import yfinance as yf
import matplotlib.pyplot as plt

datos = yf.download("EURUSD=X", period="180d", interval="1d")
precios = datos["Close"].squeeze()

# Desviacion estandar y varianza
promedio = precios.mean()
desviacion = precios.std()
varianza = precios.var()

# Bandas de Bollinger
sma_20 = precios.rolling(window=20).mean()
std_20 = precios.rolling(window=20).std()
banda_superior = sma_20 + (2 * std_20)
banda_inferior = sma_20 - (2 * std_20)

print(f"Promedio: {promedio:.4f}")
print(f"Desviacion estandar: {desviacion:.4f}")

# GRAFICO
plt.plot(precios, label="Precio de Cierre")
plt.plot(sma_20, label="SMA 20 dias")
plt.plot(banda_superior, label="Banda Superior")
plt.plot(banda_inferior, label="Banda Inferior")

plt.title("EUR/USD - Bandas de Bollinger")
plt.xlabel("Fecha")
plt.ylabel("Precio")
plt.legend()
plt.fill_between(precios.index, banda_inferior, banda_superior, alpha=0.1)
plt.show()