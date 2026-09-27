import yfinance as yf

# Descargar datos de EUR/USD de los ultimos 30 dias
datos = yf.download("EURUSD=X", period="30d", interval="1d")

print(datos["Close"])