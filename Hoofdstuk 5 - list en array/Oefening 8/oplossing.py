getallen = []
aantal_getallen = int(input("Hoeveel getallen wil je opgeven? "))
for keer in range(aantal_getallen):
    getal = int(input("Getal: "))
    getallen.append(getal)

print(f'{getallen[0]}|--|{getallen[len(getallen)//4]}--{getallen[len(getallen)//2]}--{getallen[len(getallen)//4*3]}|--|{getallen[len(getallen)-1]}')