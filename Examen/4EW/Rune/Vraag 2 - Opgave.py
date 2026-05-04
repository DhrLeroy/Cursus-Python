#Vraag 2

flessen = int(input("Aantal flesjes: "))
flessen_per_doos = int(input("Aantal flesje per doos: "))
gewicht_fles = float(input("Gewicht van een fles (zonder drank) in gram: "))
gewicht_inhoud = 260

# aantal volledige dozen
volledige_dozen = flessen // flessen_per_doos

# gewicht van één volle doos (doos + flessen)
gewicht_volle_doos =  flessen_per_doos * (gewicht_fles+gewicht_inhoud)

# totaal gewicht van alle volle dozen
totaal_gewicht_volle_dozen = (volledige_dozen * gewicht_volle_doos)/1000

print("Volledige dozen:", volledige_dozen)
print("Totaal gewicht volle dozen:", totaal_gewicht_volle_dozen, "kg")