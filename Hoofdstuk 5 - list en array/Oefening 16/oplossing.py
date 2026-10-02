volledige_naam = input("Volledige naam: ")

for positie in range(len(volledige_naam)):
    if volledige_naam[positie] == " ":
        print(f"Voornaam: {volledige_naam[0:positie]}")
        print(f"Achternaam: {volledige_naam[positie+1:]}")
        break
