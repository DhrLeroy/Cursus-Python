import sys

getal = int(input("Getal: "))

tussenstappen = []
value = getal
while(value != 1):
    if value % 2 == 0:
        value = value // 2
    else:
        value = 3*value + 1
    tussenstappen.append(value)
print(tussenstappen)