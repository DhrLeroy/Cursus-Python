afstand = float(input("Welke afstand liep je (in meter)? "))

seconden = float(input("In hoeveel seconden liep je 80 meter? "))

m_h = 80 / (seconden/(60*60))
km_h = round(m_h / 1000,2)

print(f"Je liep {km_h} km/u.")