leeftijd = int(input("Leeftijd: "))

if leeftijd >= 18:
    print("Je bent meerderjarig.")
    print("Je mag binnen!")
elif leeftijd >= 16:
    print("Je bent minderjarig, dus je mag niet binnen zonder begeleiding.")
else:
    print("Je mag niet binnen.")

print("Tot ziens")