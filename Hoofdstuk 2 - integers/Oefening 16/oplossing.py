totaal_seconden = int(input("Geef het aantal seconden: "))

uren = totaal_seconden // 3600
minuten = (totaal_seconden % 3600) // 60
seconden = totaal_seconden % 60

print(uren, "uur", minuten, "minuten en", seconden, "seconden.")