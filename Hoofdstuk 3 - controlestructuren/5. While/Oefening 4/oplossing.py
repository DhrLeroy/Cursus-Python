gevoeligheid = float(input("Gevoeligheid meetinstrument (in mg): "))
massa = float(input("Beginmassa radioactieve stof (in gram): "))

massa = massa * 1000

tijdseenheid = 0

while True:
    if massa < gevoeligheid:
        break
    tijdseenheid = tijdseenheid + 1
    print(f"Tijdseenheid {tijdseenheid}: {massa}")
    massa = massa / 2

print("De stof is niet langer detecteerbaar.")