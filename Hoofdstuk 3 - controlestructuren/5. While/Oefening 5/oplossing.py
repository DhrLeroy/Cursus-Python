temperatuur = float(input("Begintemperatuur van de vloeistof (°C): "))
omgeving = float(input("Omgevingstemperatuur (°C): "))
gewenst = float(input("Gewenste temperatuur (°C): "))

tijd = 0

while True:
    if temperatuur < gewenst:
        break
    tijd = tijd + 1
    verschil = (temperatuur - omgeving)/10
    temperatuur = temperatuur - verschil

print(f"Op minuut {tijd} werd de gewenste temperatuur bereikt.")