from math import sin, cos, asin, sqrt, degrees, radians
while True:
    entry = input("Zijde a: ")
    a = float(entry if entry else 0)
    entry = input("Zijde b: ")
    b = float(entry if entry else 0)
    entry = input("Zijde c: ")
    c = float(entry if entry else 0)
    entry = input("Hoek A (alfa): ")
    A = float(entry if entry else 0)
    entry = input("Hoek B (beta): ")
    B = float(entry if entry else 0)
    entry = input("Hoek C (gamma): ")
    C = float(entry if entry else 0)

    wijzigingen = 1
    while wijzigingen != 0:
        wijzigingen = 0
        if not A and B and C:
            A = 180 - (B + C)
            wijzigingen += 1
        if A and not B and C:
            B = 180 - (A + C)
            wijzigingen += 1
        if A and B and not C:
            C = 180 - (A + B)
            wijzigingen += 1
        if not A and a:
            if b and B:
                sinA = (a*sin(radians(B)))/b
                A = degrees(asin(sinA))
                wijzigingen += 1
            elif c and C:
                sinA = (a*sin(radians(C)))/c
                A = degrees(asin(sinA))
                wijzigingen += 1
        if not B and b:
            if a and A:
                sinB = (b*sin(radians(A)))/a
                B = degrees(asin(sinB))
                wijzigingen += 1
            elif c and C:
                sinB = (b*sin(radians(C)))/c
                B = degrees(asin(sinB))
                wijzigingen += 1
        if not C and c:
            if a and A:
                sinC = (c*sin(radians(A)))/a
                C = degrees(asin(sinC))
                wijzigingen += 1
            elif b and B:
                sinC = (c*sin(radians(B)))/b
                C = degrees(asin(sinC))
                wijzigingen += 1
        if not a and b and c and A:
            a = sqrt(b**2 + c**2 - (2*b*c*cos(radians(A))))
            wijzigingen += 1
        if not b and a and c and B:
            b = sqrt(a**2 + c**2 - (2*a*c*cos(radians(B))))
            wijzigingen += 1
        if not c and a and b and C:
            c = sqrt(a**2 + b**2 - (2*a*b*cos(radians(C))))
            wijzigingen += 1

    if a and b and c and A and B and C:
        print("Alle zijden en hoeken konden worden berekend.")
    else:
        print("Niet alle zijden en hoeken konden worden berekend.")    

    geldig = True
    if A and B and C and round(A+B+C, 1) != 180:
        geldig = False
        print(f"Ongeldige driehoek met hoeken ABC = {A}°, {B}° en {C}°. (som van hoeken is niet gelijk aan 180°)")
    if a and b and c:
        zijden = [a,b,c]
        zijden.sort()
        grootste = zijden[2]
        op_een_na_grootste = zijden[1]
        kleinste = zijden[0]
        if kleinste + op_een_na_grootste <= grootste:
            geldig = False
            print(f"Ongeldige driehoek met zijden abc = {a}, {b} en {c}. (grootste zijde is groter dan de som van de twee andere zijden)")
    if a and A and b and B and round(a/sin(radians(A)),1) != round(b/sin(radians(B)),1):
        geldig = False
        print(f"Ongeldige driehoek met zijden ab = {a}, {b} en hoeken AB = {A}° en {B}°. (sinusregel a/sin(A) = b/sin(B))")
    if a and A and c and C and round(a/sin(radians(A)),1) != round(c/sin(radians(C)),1):
        geldig = False
        print(f"Ongeldige driehoek met zijden ac = {a}, {c} en hoeken AC = {A}° en {C}°. (sinusregel a/sin(A) = c/sin(C))")
    if b and B and c and C and round(b/sin(radians(B)),1) != round(c/sin(radians(C)),1):
        geldig = False
        print(f"Ongeldige driehoek met zijden bc = {b}, {c} en hoeken BC = {B}° en {C}°. (sinusregel b/sin(B) = c/sin(C))")
    if a and b and c and A and round(a**2,1) != round(b**2 + c**2 - (2*b*c*cos(radians(A))),1):
        geldig = False
        print(f"Ongeldige driehoek met zijden abc = {a}, {b} en {c} en hoek A = {A}°. (cosinusregel a² = b² + c² - 2abcos(A))")
    if a and b and c and A and round(b**2,1) != round(a**2 + c**2 - (2*a*c*cos(radians(B))),1):
        geldig = False
        print(f"Ongeldige driehoek met zijden abc = {a}, {b} en {c} en hoek B = {B}°. (cosinusregel b² = a² + c² - 2abcos(B)")
    if a and b and c and C and round(c**2,1) != round(a**2 + b**2 - (2*a*b*cos(radians(C))),1):
        geldig = False
        print(f"Ongeldige driehoek met zijden abc = {a}, {b} en {c} en hoek C = {C}°. (cosinusregel c² = a² + b² - 2abcos(C))")
    if geldig:
        print(f"Geldige driehoek met abc = {a}, {b} en {c} en ABC = {A}°, {B}° en {C}°.")