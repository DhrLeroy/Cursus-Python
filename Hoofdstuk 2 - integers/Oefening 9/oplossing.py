prijs_euro = float(input("Prijs per stuk (excl. btw): "))
aantal = int(input("Aantal: "))
totaalbedrag_euro = prijs_euro * 1.21 * aantal

print("Totaalbedrag:",round(totaalbedrag_euro,2),"euro.")