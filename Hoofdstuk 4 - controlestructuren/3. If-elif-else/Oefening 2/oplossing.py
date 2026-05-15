temperatuurC = float(input("Wat is de voorspelde temperatuur (in C°)? "))

if temperatuurC < 0:
    print("Slipgevaar: warm de auto op")
    print("Kledij: muts, sjaal, jas")
elif temperatuurC < 10:
    print("Ontgrendel fiets")
    print("Kledij: muts, jas")
elif temperatuurC < 18:
    print("Ontgrendel fiets")
    print("Kledij: jas")
elif temperatuurC < 35:
    print("Ontgrendel fiets")
    print("Kledij: shirt en short")
else:
    print("Hittegolf: zet airco in auto aan")
    print("Kledij: shirt en short + sandalen")
