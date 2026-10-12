appel_gewicht_gr = 150
druif_gewicht_gr = 600

aantal_appels = int(input("Appels: "))
aantal_druif = int(input("Trossen druiven: "))

totaal_gewicht_gr = aantal_appels*appel_gewicht_gr + aantal_druif*druif_gewicht_gr
totaal_gewicht_kg = totaal_gewicht_gr / 1000

aantal_kisten = int(totaal_gewicht_kg // 2.5)
gewicht_zakje = totaal_gewicht_kg % 2.5

print(f"Je hebt {aantal_kisten} kistjes nodig.")
print(f"Je hebt nog een zakje nodig voor {gewicht_zakje} kg fruit.")
