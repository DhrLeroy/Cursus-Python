prijs = float(input("Prijs per stuk (excl. btw): "))
aantal = int(input("Aantal: "))
totaal = round(prijs * aantal * 1.21,2)
print(f"Totaalbedrag: {totaal} euro.")