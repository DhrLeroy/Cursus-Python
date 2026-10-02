volledige_naam = input("Volledige naam: ")

for positie in range(len(volledige_naam)):
    if volledige_naam[positie] == " ":
        voornaam = volledige_naam[0:positie]
        achternaam = volledige_naam[positie+1:]
        voornaam_2 = ""
        for letter in voornaam:
            if letter != "-":
                voornaam_2 = voornaam_2 + letter
        achternaam_2 = ""
        for letter in achternaam:
            if letter != "-" and letter != " ":
                achternaam_2 = achternaam_2 + letter
        print(f"E-mailadres: {achternaam_2}.{voornaam_2}@domein.com")
        break
