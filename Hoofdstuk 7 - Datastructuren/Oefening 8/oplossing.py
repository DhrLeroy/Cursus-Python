stack = []

while True:
    website = input("Website: ")
    if website == "stop":
        break
    stack.append(website)

while len(stack) > 0:
    input()
    website = stack.pop()
    print(f"Ga terug naar {website}")
input()
print("Startpagina")
    