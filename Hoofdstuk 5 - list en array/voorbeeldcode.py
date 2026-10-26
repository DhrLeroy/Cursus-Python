# 1 lijn commentaar

'''Meerdere
lijnen
commentaar'''

print("Hello world")

naam = "John"

print(f"Hello {naam}")
print("Hello",naam)
print("Hello "+naam)

leeftijd = 16

print("Ik ben " + str(leeftijd) + " jaar oud.")

voornaam = input("Wat is jouw voornaam? ")

lengte_cm = int(input("Hoeveel cm ben jij? "))

lengte_m = float(input("Hoeveel meter ben jij? "))

som = 1 + 2
verschil = 2 - 1
product = 2 * 3
quotiënt = 2 / 3
gehele_deling = 2 // 3
rest_na_deling = 3 % 2
macht = 2 ** 3

from math import *
vierkantswortel = sqrt(4)

prijs = float(input("Prijs: "))
if prijs > 20:
    print("Gratis verzending.")

if prijs >= 20:
    print("Prijs is groter of gelijk aan 20.")
    print("Gratis verzending.")

if prijs == 20:
    print("Prijs is gelijk aan 20.")
else:
    print("Prijs is niet gelijk aan 20.")

if prijs < 20:
    print("Prijs is kleiner dan 20.")
elif prijs == 20:
    print("Prijs is gelijk aan 20.")
else:
    print("Prijs is groter dan 20.")

verzendkost = 3 if prijs > 20 else 0

aantal = 1
while aantal < 10:
    aantal += 1

aantal = 1
while True:
    aantal += 1
    if aantal == 10:
        break

for i in range(11):
    print(i)

for i in range(1,21):
    if i % 2 == 0:
        continue
    print(i)

for i in range(1,21,2):
    print(i)

lijst = [1,2,3]
lijst.append(4)
lijst.append(5)
lijst.append(6)

for item in lijst:
    print(item)

for positie in range(len(lijst)):
    lijst[positie] = lijst[positie] * -1

lijst_omgedraaid = lijst[::-1]

eerste_3_items = lijst[0:3]

vanaf_4de_item = lijst[3:]

laatst_3_items = lijst[-3:]






print()