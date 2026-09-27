import yfinance as yf
import matplotlib.pyplot as plt

# Descargar datos de EUR/USD de los ultimos 30 dias
datos = yf.download("EURUSD=X", period="30d", interval="1d")
# Media movil simple basada en los anteriores 5 dias
datos["SMA_5"] = datos["Close"].rolling(window=5).mean()

# RSI Relative Strength Index (Indice de Fuerza Relativa)
# 1. Calcular el cambio diario
delta = datos["Close"].squeeze().diff()
# 2. Separar ganancias (subidas) y perdidas (bajadas)
ganancia = delta.where(delta > 0, 0)
perdida = -delta.where(delta < 0, 0)
# 3. Promedio movil de ganancias y perdidas (estandar de 14 dias)
media_ganancia = ganancia.rolling(window=14).mean()
media_perdida = perdida.rolling(window=14).mean()
# 4. Formula del RSI
rs = media_ganancia / media_perdida
rsi = 100 - (100 / (1 + rs))

datos["RSI"] = rsi

print("Clase 6 y 7")
print(datos[["Close", "RSI"]])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

# Grafico 1: Precio + SMA
ax1.plot(datos["Close"].squeeze(), label="Precio de cierre")
ax1.plot(datos["SMA_5"].squeeze(), label="Media movil 5 dias")
ax1.set_title("EUR/USD - Precio y SMA")
ax1.set_xlabel("Fecha")
ax1.set_ylabel("Precio")
ax1.legend()

# Grafico 2: RSI
ax2.plot(datos["RSI"])
ax2.axhline(70, color="grey", linestyle="--", label="Sobrecompra (70)")
ax2.axhline(30, color="grey", linestyle="--", label="Sobreventa (30)")
ax2.set_title("EUR/USD - RSI")
ax2.set_xlabel("Fecha")
ax2.set_ylabel("RSI")
ax2.legend()

# Correr graficos
plt.tight_layout()
plt.show()