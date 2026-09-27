precios = [1.070, 1.075, 1.078, 1.082, 1.079, 1.085, 1.090]
nivel_soporte = 1.075
nivel_resistencia = 1.085

for precio in precios:
    if precio >= nivel_resistencia:
        print("Ruptura alcista")
    elif precio <= nivel_soporte:
        print("Ruptura bajista")
    else:
        print("En rango")