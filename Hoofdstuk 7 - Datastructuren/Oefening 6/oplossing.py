from collections import deque

planning = deque()

while True:
    keuze = input("Wat wil je doen (studeren / plannen)? ")
    if keuze == "plannen":
        studieblok = input("Studieblok: ")
        planning.append(studieblok)
    elif keuze == "studeren":
        studieblok = planning.popleft()
        print(f"Studeer nu {studieblok}.")
