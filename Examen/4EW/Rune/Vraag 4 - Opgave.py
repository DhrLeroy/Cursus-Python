#Vraag 4

temps = []
totaal_temps = 0

for dag in range(7):
    temp = float(input("Temperatuur (in °C): "))
    temps.append(temp)
    totaal_temps = totaal_temps + temp

gemiddelde = totaal_temps/7

print("Gemiddelde temperatuur:",gemiddelde,"°C")



