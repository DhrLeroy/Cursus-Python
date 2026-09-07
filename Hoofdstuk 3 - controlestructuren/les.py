getal = int(input("Getal: "))

if getal > 0:
    print(f"{getal} is strikt positief.")
else:
    if getal == 0:
        print(f'{getal} is 0')
    else:
        print(f"{getal} is strikt negatief.")

maand_getal = int(input("Maand: "))µ

if maand_getal == 1:
    print("Januari")
elif maand_getal == 2:
    print("Februari")
elif maand_getal == 12:
    print("December")


















input()



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





leeftijd = int(input("Leeftijd: "))

if leeftijd >= 18:
    print("Meerderjarig")
elif leeftijd <= 1:
    print("Baby")
else:
    print("Kind")