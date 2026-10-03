prijs = float(input("Geef de prijs (in euro) in die destijds werd betaald: "))
jaartal = int(input("In welk jaartal heb je dit gekocht? "))
maand = int(input("In welke maand van 2001 heb je dit gekocht (cijfer)? "))

while True:
    if jaartal == 2026:
        if maand == 6:
            break
    maand = maand + 1
    prijs = prijs * 1.012
    if maand == 13:
        maand = 1
        jaartal = jaartal + 1

print(f"Actuele prijs in juni 2026: {round(prijs,2)} euro.")
