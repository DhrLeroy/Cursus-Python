liedjes = []

while True:
    liedje = input("Liedje: ")
    if liedje == "klaar":
        break
    liedjes.append(liedje)

while True:
    verwijderen = input("Welk liedje verwijderen? ")
    if verwijderen == "":
        break
    liedjes.remove(verwijderen)

print(f'Het feestje begint met "{liedjes[0]}" en eindigt met "{liedjes[-1]}".')
print("Playlist:")
for teller in range(len(liedjes)):
    print(f"{teller+1}. {liedjes[teller]}")