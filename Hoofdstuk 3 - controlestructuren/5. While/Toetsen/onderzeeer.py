max_druk = float(input("Maximale druk (bar): "))*100000
gewenste_diepte = float(input("Gewenste diepte (m): "))

P0 = 101325
rho = 1025
g = 9.81

diepte = 0
druk = P0
minuten = 0

while diepte < gewenste_diepte and druk <= max_druk:
    extra_daling = float(input("Hoeveel meter werd deze minuut extra gedaald? "))

    diepte += extra_daling
    minuten += 1

    druk = P0 + rho * g * diepte

if druk > max_druk:
    reden = "De maximale druk werd overschreden."
else:
    reden = "De gewenste diepte werd bereikt."

print()
print(reden)
print(f"Aantal minuten: {minuten}")
print(f"Bereikte diepte: {round(diepte,2)} m")
print(f"Druk: {round(druk,2)} Pa")