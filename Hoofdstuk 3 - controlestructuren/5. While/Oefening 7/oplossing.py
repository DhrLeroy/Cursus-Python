getal = int(input("Getal: "))

output = f"{getal}: "
while True:
    if getal % 2 == 0:
        getal /= 2
    else:
        getal = 3*getal+1
    output += f"{int(getal)}"
    if getal != 1:
        output += ", "
    else:
        break

print(output)