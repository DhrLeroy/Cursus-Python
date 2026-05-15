onvoldoendes = int(input("Hoeveel onvoldoendes heb je? "))

if onvoldoendes > 3:
    print("Negatief advies")
else:
    totaal = float(input("Hoeveel is jouw totaalgemiddelde? "))
    if totaal < 0.5:
        print("Voorwaardelijk advies")
    else:
        if onvoldoendes < 2:
            print("Positief advies")
        else:
            print("Voorwaardelijk advies")