snelheid_km_u = float(input("Snelheid (km/u): "))

remafstand_m = snelheid_km_u/2
reactieafstand_m = 5

if 50 <= snelheid_km_u <= 90:
    reactieafstand_m = 25

if snelheid_km_u > 90:
    reactieafstand_m = 30

stopafstand_m = remafstand_m + reactieafstand_m

print("Stopafstand:",stopafstand_m,"m")