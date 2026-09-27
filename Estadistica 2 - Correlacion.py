# CORRELACION
import yfinance as yf
import matplotlib.pyplot as plt

# Descargar dos pares distintos. Solo los precios de cierre
eur_usd = yf.download("EURUSD=X", period="180d", interval="1d")["Close"].squeeze()
gbp_usd = yf.download("GBPUSD=X", period="180d", interval="1d")["Close"].squeeze()

correlacion = eur_usd.corr(gbp_usd)
print(f"Correlacion EUR/USD vs GBP/USD: {correlacion:.4f}")

# GRAFICOS

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))

ax1.plot(eur_usd, label="EUR/USD", color="blue")
ax1.set_title("EUR/USD")
ax1.legend()

ax2.plot(gbp_usd, label="GBP/USD", color="orange")
ax2.set_title("GBP/USD")
ax2.legend()

# Visualizar grafico de dispersion
ax3.scatter(eur_usd, gbp_usd, alpha=0.5)
ax3.set_title("Correlacion EUR/USD vs GBP/USD")
ax3.set_xlabel("EUR/USD")
ax3.set_ylabel("GBP/USD")

plt.tight_layout()
plt.show()