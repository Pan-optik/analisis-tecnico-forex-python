precio_actual = 1.272
nivel_soporte = 1.26
nivel_resistencia = 1.28

if precio_actual > nivel_soporte and precio_actual >= nivel_resistencia:
    print(f"Precio actual: {precio_actual} Posible ruptura alcista")
elif precio_actual > nivel_soporte and precio_actual < nivel_resistencia:
    print(f"Precio actual: {precio_actual} En rango")
else:
    print(f"Precio actual: {precio_actual} Posible ruptura bajista")