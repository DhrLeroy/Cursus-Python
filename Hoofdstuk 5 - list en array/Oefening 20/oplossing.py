geboortejaar = input("Geboortejaar: ")
rijksregisternummer = input("Rijksregisternummer: ")

geboortejaar_jj = geboortejaar[2:]
rijksregisternummer_jj = rijksregisternummer[:2]

if geboortejaar_jj != rijksregisternummer_jj:
    print("Geboortejaar niet correct in rijksregisternummer")
if len(rijksregisternummer) != 11:
    print("Rijksregisternummer te lang of te kort.")

rijksregisternummer_deel1 = rijksregisternummer[0:9]
if int(geboortejaar) >= 2000:
    rijksregisternummer_deel1 = "2"+rijksregisternummer_deel1

rijksregisternummer_controlegetal = rijksregisternummer[9:]

rest = int(rijksregisternummer_deel1) % 97
controlegetal = 97 - rest

if rijksregisternummer_controlegetal == str(controlegetal):
    print("Controlegetal klopt.")
else:
    print("Controlegetal klopt niet.")