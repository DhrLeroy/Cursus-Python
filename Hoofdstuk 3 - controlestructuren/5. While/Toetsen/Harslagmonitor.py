rust = int(input("Wat is je rusthartslag? "))
minuten = 0

hartslag = 0
while True:
    minuten = minuten + 1
    invoer = input(f"Minuut {minuten}: Wat is je hartslag? ")
    if invoer == "STOP":
        break
    hartslag = int(invoer)

while hartslag > rust:
    hartslag = hartslag * 0.85
    minuten = minuten + 1

print(f"Je kwam tot rust in minuut {minuten}.")
