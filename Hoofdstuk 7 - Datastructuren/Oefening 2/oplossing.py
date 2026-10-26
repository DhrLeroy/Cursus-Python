stack = []

while True:
    datum = input("Vervaldatum: ")
    if datum == "aangevuld":
        break
    stack.append(datum)
input()
volgende_vervaldatum = stack.pop()
print(f"Dit product vervalt op {volgende_vervaldatum}")