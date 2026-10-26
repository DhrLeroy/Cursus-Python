from collections import deque

leerlingen = deque()

while True:
    leerling = input("Leerling: ")
    if leerling == "11u10":
        break
    leerlingen.append(leerling)

while len(leerlingen) > 0:
    leerling = leerlingen.popleft()
    print(f"{leerling} mag afgeven")
    input()