from collections import deque

taakplanning = deque()

while True:
    taak = input("Wat wil je doen? ")
    if taak.lower() == "stop":
        break
    else:
        taakplanning.append(taak)

for taakitem in range(len(taakplanning)):
    input()
    print(taakplanning.popleft())
