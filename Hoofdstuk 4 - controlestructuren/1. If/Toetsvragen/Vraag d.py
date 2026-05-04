

zonintensiteit = float(input("Zonintensiteit (W/m²): "))
basis = zonintensiteit / 200

extra = 0
buiten = float(input("Buitentemperatuur (°C): "))
if buiten < 15:
    extra = -2
if buiten > 25:
    extra = 3

temperatuur = basis + extra

print("Temperatuur:",temperatuur,"°C")