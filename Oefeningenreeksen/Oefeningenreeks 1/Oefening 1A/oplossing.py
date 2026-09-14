import sys

for teller in range(1, sys.maxsize):
    tussenstappen = []
    value = teller
    while(value != 1):
        if value % 2 == 0:
            value = value // 2
        else:
            value = 3*value + 1
        tussenstappen.append(value)
    with open("Oefeningenreeksen\\Oefeningenreeks 1\\Oefening 1A\\collatz.txt", "a") as file:
        file.write(f"{teller}: {tussenstappen}\n")