basisprijs_euro = float(input("Basisprijs (in euro, excl. btw): "))
aantal = int(input("Aantal: "))
categorie = input("Categorie: ")

btw_tarief = 0.21

if categorie == "fruit":
    btw_tarief = 0.06
if categorie == "groenten":
    btw_tarief = 0.06
if categorie == "boeken":
    btw_tarief = 0.12

totaalprijs = (basisprijs_euro * (1+btw_tarief)) * aantal

print(f"Totaal: {totaalprijs} euro.")