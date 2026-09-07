score = float(input("Behaald: "))
totaal = float(input("Totaal: "))
percentage = score/totaal

if score < 0.3:
    print("Rood")
else:
    if score < 0.5:
        print("Oranje")
    else:
        if score < 0.7:
            print("Geel")
        else:
            if score < 0.9:
                print("Groen")
            else:
                print("Blauw")