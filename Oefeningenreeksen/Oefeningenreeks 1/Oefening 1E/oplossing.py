getal1 = int(input("Getal 1: "))
getal2 = int(input("Getal 2: "))

deler = min(getal1, getal2)

while deler >= 1:
    if getal1 % deler == 0 and getal2 % deler == 0:
        break
    deler -= 1

print(f"De grootste gemeenschappelijk deler van {getal1} en {getal2} is {deler}.")

veelvoud1 = getal1
veelvoud2 = getal2

while veelvoud1 != veelvoud2:
    if veelvoud1 < veelvoud2:
        veelvoud1 += getal1
    else:
        veelvoud2 += getal2

print(f"Het kleinst gemeenschappelijke veelvoud van {getal1} en {getal2} is {veelvoud1}.")
