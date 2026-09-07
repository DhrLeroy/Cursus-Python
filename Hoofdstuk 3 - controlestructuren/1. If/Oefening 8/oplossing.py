seconden = float(input("Seconden: "))

maximale_tijdsduur_uur = 1.6/30

maximale_tijdsduur_seconden = maximale_tijdsduur_uur * 60 * 60

if seconden > maximale_tijdsduur_seconden:
    print("85 euro boete!")