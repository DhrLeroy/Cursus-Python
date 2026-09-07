snelheid = float(input("Beginsnelheid meteoriet (m/s): "))

seconden = 0

while True:
    vorige_snelheid = snelheid
    seconden = seconden + 1
    snelheid = (snelheid + 9.81)*0.95
    if snelheid - vorige_snelheid < 0.2:
        break

print(f"De meteoriet haalde een topsnelheid van {snelheid} m/s na {seconden} seconden.")