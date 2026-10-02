getal = int(input("Getal: "))
som = 0
for cijfer in str(getal):
    som = som + int(cijfer)**len(str(getal))
if som == getal:
    print(f"{getal} is een narcistisch getal.")
else:
    print(f"{getal} is geen narcistisch getal.")
