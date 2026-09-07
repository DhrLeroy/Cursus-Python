punten = []
totalen = []

while True:
    behaald = input("Behaald: ")
    if behaald == "STOP":
        break
    op = input("Op: ")
    behaald = float(behaald)
    op = float(op)
    if behaald > op:
        continue
    if op <= 0:
        continue
    punten.append(behaald)
    totalen.append(op)

totaal = 0
maximum = 0
for i in range(len(punten)):
    totaal = totaal + punten[i]
    maximum = maximum + totalen[i]

percentage = totaal / maximum

print(f"Er werden {len(punten)} toetsen ingegeven.")

print(f"Je hebt een gemiddelde van {percentage*100}%.")