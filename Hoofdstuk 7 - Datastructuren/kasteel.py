stack = []

print("Je bent in de Inkomhal")

while True:

    uitgangen = []

    aantal = int(input("Hoeveel uitgangen? "))

    for teller in range(aantal):
        kamer = input(f"{teller + 1}e kamer: ")
        uitgangen.append(kamer)

    while True:

        print("\nMogelijke kamers:")

        for teller in range(len(uitgangen)):
            print(f"{teller + 1}. {uitgangen[teller]}")

        keuze = input("Keuze (nummer, terug of stop): ")

        if keuze == "stop":
            quit()

        elif keuze == "terug":

            if len(stack) == 0:
                print("Je bent terug in de inkomhal.")
            else:
                uitgangen = stack.pop()
                print("Je bent teruggekeerd.")

        else:
            nummer = int(keuze) - 1

            stack.append(uitgangen)

            print(f"\nJe bent in {uitgangen[nummer]}")
            break