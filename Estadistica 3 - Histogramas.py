import yfinance as yf
import matplotlib.pyplot as plt

datos = yf.download("EURUSD=X", period="180d", interval="1d")
precios = datos["Close"].squeeze()
variacion = precios.pct_change() * 100

p10 = variacion.quantile(0.10)
p90 = variacion.quantile(0.90)
print(f"Percentil 10: {p10:.4f}%")
print(f"Percentil 90: {p90:.4f}%")

plt.hist(variacion.dropna(), bins=30, edgecolor="white")
plt.axvline(p10, color=(0.6, 0, 0, 0.5), linestyle="--", label=f"Percentil 10 ({p10:.2f}%)")
plt.axvline(p90, color=(0, 0.6, 0, 0.5), linestyle="--", label=f"Percentil 90 ({p90:.2f}%)")
plt.title("Distribucion de variaciones diarias - EUR/USD")
plt.xlabel("Variacion %")
plt.ylabel("Frecuencia")
plt.legend()

plt.show()