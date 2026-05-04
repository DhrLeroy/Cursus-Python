

snelheid = float(input("Snelheid (km/u): "))

stopafstand = snelheid/2
reactieafstand = 5

if 50 <= snelheid <= 90:
    reactieafstand = 25

if snelheid > 90:
    reactieafstand = 30

remafstand = stopafstand + reactieafstand

print("Remafstand:",remafstand,"m")