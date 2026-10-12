interestvoet = float(input("Jaarlijkse interestvoet: "))/100
aantal_jaar = int(input("Aantal jaar: "))
bedrag = 100

totaal = round(bedrag * ((1+(interestvoet/12))**(12*aantal_jaar)),2)

print(f"Totaalbedrag na {aantal_jaar} jaar: {totaal}")
