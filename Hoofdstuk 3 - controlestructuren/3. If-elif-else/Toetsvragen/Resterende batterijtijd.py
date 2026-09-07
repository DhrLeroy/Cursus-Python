batterijpercentage = float(input("Geef het batterijpercentage: "))

resterende_tijd_minuten = 0

if batterijpercentage < 20:
    resterende_tijd_minuten = batterijpercentage * 3.2
else:
    stand = input("Welke stand? (eco/normaal/hoog): ")
    if stand == "eco":
        resterende_tijd_minuten = batterijpercentage * 3.2
    elif stand == "normaal":
        resterende_tijd_minuten = 20 * 3.2 + (batterijpercentage - 20) * 2.7
        # of zoals het voorbeeld
        # resterende_tijd_minuten = batterijpercentage * 2.7
    elif stand == "hoog":
        resterende_tijd_minuten = 20 * 3.2 + (batterijpercentage - 20) * 2.1
        # of zoals het voorbeeld
        # resterende_tijd_minuten = batterijpercentage * 2.1
    else:
        print("Ongeldige stand")

if resterende_tijd_minuten != 0:
    print(f"Resterende tijd: {resterende_tijd_minuten} minuten.")