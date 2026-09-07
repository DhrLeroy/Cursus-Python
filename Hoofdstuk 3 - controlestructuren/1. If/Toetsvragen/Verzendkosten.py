prijs_euro = float(input("Aankoopprijs (in euro): "))
gewicht_kg = int(input("Gewicht (in kg): "))

if 3 <= gewicht_kg < 20:
    prijs_euro = prijs_euro + (gewicht_kg-3)*0.5

if gewicht_kg >= 20:
    prijs_euro = prijs_euro + 17*0.5 + (gewicht_kg-19)*0.8

print(f"Totaalprijs: {round(prijs_euro,2)} euro")