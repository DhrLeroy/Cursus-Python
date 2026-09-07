gewicht_aarde = float(input("Gewicht (op Aarde, in Newton): "))

massa = gewicht_aarde / 9.81

ruimtelichaam = input("Kies een ruimtelichaam (Maan, Mars, Jupiter): ")

zwaartekrachtsversnelling = 0

if ruimtelichaam == "Maan":
    zwaartekrachtsversnelling = 1.62
if ruimtelichaam == "Mars":
    zwaartekrachtsversnelling = 3.71
if ruimtelichaam == "Jupiter":
    zwaartekrachtsversnelling = 24.79

print(f'Jouw gewicht op {ruimtelichaam} is {massa*zwaartekrachtsversnelling} Newton.')