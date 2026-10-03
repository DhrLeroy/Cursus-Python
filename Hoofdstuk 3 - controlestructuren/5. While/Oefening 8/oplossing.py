totaalbedrag = 0

basisprijs = input("Basisprijs (in euro): ")

while basisprijs != "STOP":
    basisprijs_euro = float(basisprijs)
    aantal = int(input("Aantal stuks: "))
    btw_tarief = float(input("BTW-tarief (6%, 12%, 21%): "))

    prijs = basisprijs_euro * (100+btw_tarief) / 100 * aantal

    totaalbedrag += prijs

    basisprijs = input("Basisprijs (in euro): ")

print(f"Totale factuurprijs: {totaalbedrag} euro.")
