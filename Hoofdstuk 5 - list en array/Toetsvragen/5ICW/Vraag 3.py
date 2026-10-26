games = []

for i in range(5):
    titel = input(f"Geef game {i + 1}: ")
    games.append(titel)

for i in range(len(games)):
    personage = input(f"Wat is jouw favoriete personage uit {games[i]}? ")
    games[i] = games[i] + " (" + personage + ")"

print(f"Alle games: {games}")