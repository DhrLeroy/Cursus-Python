leeftijd = int(input("Leeftijd: "))

maximale_hartslag = 208 - (leeftijd*0.7)

hartslag = int(input("Hartslag: "))

percentage = (hartslag / maximale_hartslag) * 100

if percentage < 60:
    print("Lichte inspanning")

if 60 <= percentage <= 80:
    print("Matige inspanning")

if percentage > 80:
    print("Zware inspanning")