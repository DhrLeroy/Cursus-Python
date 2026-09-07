spanning_volt = 230
stroom_ampère = int(input("Stroom van toestel (in ampère): "))

vermogen_watt = spanning_volt * stroom_ampère

if vermogen_watt <= 2300:
    print("Alles is veilig")

if 2300 < vermogen_watt <= 3680:
    print("Let op: kans op oververhitting")

if vermogen_watt > 3680:
    print("Opgelet: overbelasting!")