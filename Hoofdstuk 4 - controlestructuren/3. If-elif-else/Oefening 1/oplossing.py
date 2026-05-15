score = float(input("Behaald: "))
totaal = float(input("Totaal: "))
percentage = score/totaal

if score < 0.3:
    print("Rood")
elif score < 0.5:
    print("Oranje")
elif score < 0.7:
    print("Geel")
elif score < 0.9:
    print("Groen")
else:
    print("Blauw")