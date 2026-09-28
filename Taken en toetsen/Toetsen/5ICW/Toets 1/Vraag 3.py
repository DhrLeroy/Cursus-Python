product = input("Wat kochten jullie aan? ")
aantal = int(input(f"Hoeveel {product} hebben jullie gekocht? "))
personen = int(input("Met hoeveel waren jullie? "))
aantal_per_persoon = aantal // personen
print(f"Ieder krijgt {aantal_per_persoon} {product}.")
rest = aantal % personen
print(f"Er zijn nog {rest} resterende {product} over.")