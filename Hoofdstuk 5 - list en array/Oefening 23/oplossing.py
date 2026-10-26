isbn = input("Geef een ISBN-13 in: ")

som = 0

for i in range(12):
    cijfer = int(isbn[i])

    if i % 2 == 0:
        som += cijfer
    else:
        som += cijfer * 3

controlecijfer = (10 - (som % 10)) % 10

if controlecijfer == int(isbn[12]):
    print("Geldige ISBN-code.")
else:
    print("Ongeldige ISBN-code.")