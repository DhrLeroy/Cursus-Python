bewusteloos = input("Is de patiënt bewusteloos? ")

if bewusteloos == "Ja":
    print("Dringende hulp")
else:
    pijnscore = float("Pijnscore (op 10): ")
    if pijnscore > 8:
        print("Dringende hulp")
    else:
        print("Patiënt kan wachten")