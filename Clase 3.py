par = "EUR/USD"

datos = [
    {"fecha": "2026-09-07", "precio": 1.070},
    {"fecha": "2026-09-08", "precio": 1.075},
    {"fecha": "2026-09-09", "precio": 1.078},
    {"fecha": "2026-09-10", "precio": 1.082},
    {"fecha": "2026-09-11", "precio": 1.077},
    {"fecha": "2026-09-12", "precio": 1.090},
    {"fecha": "2026-09-13", "precio": 1.089},
    {"fecha": "2026-09-14", "precio": 1.085}
]

soporte = 1.075
resistencia = 1.085

for vela in datos:
    if vela["precio"] >= resistencia:
        print(f"{vela['fecha']}: {vela['precio']} --> Ruptura Alcista")
    elif vela["precio"] <= soporte:
        print(f"{vela['fecha']}: {vela['precio']} --> Ruptura Bajista")
    else:
        print(f"{vela['fecha']}: {vela['precio']} --> En Rango")