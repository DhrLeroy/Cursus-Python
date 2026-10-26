hartslag = float(input("Hartslag: "))
leeftijd = int(input("Leeftijd: "))

maximale_hartslag = 208 - (leeftijd*0.7)

verhouding = hartslag / maximale_hartslag

if verhouding < 0.6:
    print("Lichte inspanning")
if 0.6 <= verhouding < 0.8:
    print("Matige inspanning")
if verhouding > 0.8:
    print("Zware inspanning")
    