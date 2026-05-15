punten = []

while True:
    punt = float(input("Resultaat: "))
    if punt < 0:
        break
    punten.append(punt)
    if len(punten) > 10:
        break

print(punten)









getal = int(input("Getal: "))

while getal < 1000:
    print(getal * 2)

print(getal)





leeftijd = 0

while leeftijd <= 0:
    leeftijd = int(input("Leeftijd: "))

print(f'Je bent {leeftijd} jaar oud.')