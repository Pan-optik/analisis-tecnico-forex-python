import yfinance as yf

# Descargar datos de EUR/USD de los ultimos 30 dias
datos = yf.download("EURUSD=X", period="30d", interval="1d")

print("Clase 5")

# print(datos["Close"])

datos["Variacion_%"] = datos["Close"].pct_change() * 100
datos["SMA_5"] = datos["Close"].rolling(window=5).mean()

print(datos[["Close", "Variacion_%", "SMA_5"]])

soporte = datos["Close"].squeeze().min()
resistencia = datos["Close"].squeeze().max()

for fecha, precio in datos["Close"].squeeze().items():
    if precio >= resistencia:
        print(f"{fecha.date()}: {precio:.4f} --> Ruptura alcista")
    elif precio <= soporte:
        print(f"{fecha.date()}: {precio:.4f} --> Ruptura bajista")
    else:
        print(f"{fecha.date()}: {precio:.4f} --> En rango")
