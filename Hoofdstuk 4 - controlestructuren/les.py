leeftijd = int(input("Leeftijd: "))

for teller in range(1,6):
    print(teller)

if leeftijd >= 18:
    print("Meerderjarig")

if leeftijd > 17:
    print("Meerderjarig")

if leeftijd <= 17:
    print("Minderjarig")

if leeftijd < 18:
    print("Minderjarig")

if leeftijd == 0:
    print("Welkom op de wereld")

if not leeftijd == 0:
    print("Jij was al geboren")

if leeftijd != 0:
    print("Jij was al geboren")

keuze = input("Oefen jij graag Python (y/n)?")
if keuze == "y":
    print("Ik ook!")

python_is_leuk = keuze == "y"

if python_is_leuk:
    print("Ik ook!")


print("Gedaan")

