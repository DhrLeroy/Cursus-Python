gecodeerd = input("Geef de gecodeerde boodschap in: ")

# De boodschap bestaat uit 4 gelijke delen
lengte_deel = len(gecodeerd) // 4

deel1 = gecodeerd[:lengte_deel]
deel2 = gecodeerd[lengte_deel:2 * lengte_deel]
deel3 = gecodeerd[2 * lengte_deel:3 * lengte_deel]
deel4 = gecodeerd[3 * lengte_deel:]

# Eerste en derde deel terug omdraaien
deel1 = deel1[::-1]
deel3 = deel3[::-1]

# Eerste en derde deel terug van plaats wisselen
oorspronkelijk = deel3 + deel2 + deel1 + deel4

print("Oorspronkelijke boodschap:", oorspronkelijk)