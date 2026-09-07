zonintensiteit_W_m2 = float(input("Zonintensiteit (W/m²): "))
basistemperatuur_C = zonintensiteit_W_m2 / 200

extra_temperatuur = 0
buitentemperatuur_C = float(input("Buitentemperatuur (°C): "))
if buitentemperatuur_C < 15:
    extra_temperatuur = -2
if buitentemperatuur_C > 25:
    extra_temperatuur = 3

binnentemperatuur_C = basistemperatuur_C + extra_temperatuur

print("Temperatuur:",binnentemperatuur_C,"°C")