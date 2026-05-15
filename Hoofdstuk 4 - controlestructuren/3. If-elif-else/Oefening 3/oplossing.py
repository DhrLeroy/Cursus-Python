dagnummer_maandag = int(input("Dagnummer van eerste maandag: "))
dagnummer = int(input("Dagnummer van dag: "))

verschil_maandag = (dagnummer - dagnummer_maandag)%7

if verschil_maandag == 0:
    print("Maandag")
elif verschil_maandag == 1:
    print("Dinsdag")
elif verschil_maandag == 2:
    print("Woensdag")
elif verschil_maandag == 3:
    print("Donderdag")
elif verschil_maandag == 4:
    print("Vrijdag")
elif verschil_maandag == 5:
    print("Zaterdag")
else:
    print("Zondag")
