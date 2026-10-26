diepte_m = float(input("Geef de diepte in meter: "))

druk_pascal = 1025 * 9.81 * diepte_m

druk_bar = round(druk_pascal / 100000,2)

print("Totale druk:",druk_bar,"bar.")