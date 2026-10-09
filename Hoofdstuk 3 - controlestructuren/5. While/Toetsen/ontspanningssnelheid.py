massa = float(input("Massa van de raket (ton): "))
kracht = float(input("Stuwkracht (kN): "))

snelheid = 0
tijd = 0

while snelheid < 11200:
    snelheid += kracht / massa
    tijd += 1

print(f"Ontsnappingssnelheid bereikt na {tijd} seconden.")