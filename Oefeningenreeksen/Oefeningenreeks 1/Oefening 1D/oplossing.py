import sys

for i in range(1,sys.maxsize):
    getal = str(i)
    som = 0
    termen = ""
    for j in range(len(getal)):
        term = int(getal[j])**len(getal)
        som += term
        termen += f" + {term}"
    if som == i:
        print(f"{i} is een narcistisch getal want {i} = {termen[3:]}")
