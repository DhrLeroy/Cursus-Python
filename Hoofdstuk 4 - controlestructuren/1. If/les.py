leeftijd = int(input("Leeftijd: "))

if leeftijd >= 18:
    tickets = int(input("Aantal tickets: "))
    if tickets <= 0:
        print("Je moet minstens 1 ticket kopen.")
    else:
        print(f'Je hebt {tickets} tickets besteld.')
else:
    print("Je bent te jong om tickets te kopen.") 

    