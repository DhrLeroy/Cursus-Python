getal = int(input("Getal: "))
kwadraat = getal ** 2
kwadraat_str = str(kwadraat)
aantal_cijfers = len(str(getal))
rechter_deel = kwadraat_str[-aantal_cijfers:]
linker_deel = kwadraat_str[0:len(kwadraat_str)-len(rechter_deel)]
int_links = 0
if linker_deel == "":
    int_links = 0
else:
    int_links = int(linker_deel)
int_rechts = int(rechter_deel)
if int_links + int_rechts and int_rechts != 0:
    print(f"{getal} is geen Kaprekar-getal.")
else:
    print(f"{getal} is geen Kaprekar-getal.")