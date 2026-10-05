iban = input("Geef het IBAN-rekeningnummer in: ")
iban_zonder_spatie = iban[0:4]+iban[5:9]+iban[10:14]+iban[15:19]
landcode = iban_zonder_spatie[0:2]
controle = iban_zonder_spatie[2:4]
rest = iban_zonder_spatie[4:]

test = rest
for letter in landcode:
    if letter == "A":
        test = test + "10"
    elif letter == "B":
        test = test + "11"
    elif letter == "C":
        test = test + "12"
    elif letter == "D":
        test = test + "13"
    elif letter == "E":
        test = test + "14"
test = test + controle

print(test)

print(int(test) % 97 )

wel_niet = "een" if int(test) % 97 == 1 else "geen"

print(f"{iban} is {wel_niet} geldig rekeningnummer.")