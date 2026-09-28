telefoonnummer = input("Telefoonnummer: ")
geldig = False

if telefoonnummer[0:5]=="00324":
    if len(telefoonnummer) == 13:
        geldig = True
elif telefoonnummer[0:2]=="04":
    if len(telefoonnummer) == 10:
        geldig = True
elif telefoonnummer[0:4]=="+324":
    if len(telefoonnummer) == 12:
        geldig = True

cijfers = "0123456789"
for positie in range(len(telefoonnummer)):
    if telefoonnummer[positie] == " " or telefoonnummer[positie] == "-" or (telefoonnummer[positie] == "+" and positie != 0):
        geldig = False

if geldig:
    gemaskeerd = ""
    for aantal in range(len(telefoonnummer)-2):
        gemaskeerd = gemaskeerd+"*"
    gemaskeerd = gemaskeerd+telefoonnummer[len(telefoonnummer)-2:]
    print(gemaskeerd)
else:
    print("Ongeldig telefoonnummer")