U = 230
I = int(input("Stroom van toestel (in ampère): "))

P = U * I

if P <= 2300:
    print("Alles is veilig")

if 2300 < P <= 3680:
    print("Let op: kans op oververhitting")

if P > 3680:
    print("Opgelet: overbelasting!")