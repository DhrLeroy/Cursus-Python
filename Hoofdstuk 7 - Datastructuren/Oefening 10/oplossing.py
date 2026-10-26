from collections import deque

wachtrij = deque()

while True:
    naam = input("Naam: ")
    if naam == "open":
        break
    wachtrij.append(naam)

while len(wachtrij) > 0:
    naam = wachtrij.popleft()
    print(f"{naam} mag instappen.")