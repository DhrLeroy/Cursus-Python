temperaturen = []

# Temperaturen inlezen
for dag in range(1, 8):
    temperatuur = float(input(f"Temperatuur dag {dag} (in °C): "))
    temperaturen.append(temperatuur)

# Foutieve temperaturen controleren
for i in range(1, len(temperaturen) - 1):
    huidige = temperaturen[i]
    vorige = temperaturen[i - 1]
    volgende = temperaturen[i + 1]

    fout_tov_vorige = huidige > vorige * 1.5 or huidige < vorige * 0.5
    fout_tov_volgende = huidige > volgende * 1.5 or huidige < volgende * 0.5

    if fout_tov_vorige and fout_tov_volgende:
        temperaturen[i] = float(input(f"Geef een nieuwe temperatuur in voor dag {i + 1} ({huidige}°C): "))

som = 0
for temp in temperaturen:
    som = som + temp

gemiddelde = round(som / len(temperaturen),1)

print(f"Gemiddelde weektemperatuur: {gemiddelde}°C")