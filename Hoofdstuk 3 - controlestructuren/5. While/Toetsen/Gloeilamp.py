huidig_licht_procent = float(input("Hoe helder schijnt de lamp nog (in %)? "))

licht_procent = 100
seconden = 0

while licht_procent > huidig_licht_procent:
    seconden = seconden + 1
    licht_procent = licht_procent * 0.88

print(f"De stroom ligt al {seconden} seconden af.")