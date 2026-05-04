#Vraag 5

P = float(input("Geleend bedrag (P): "))
r = float(input("Maandelijkse rentevoet (r): "))
n = int(input("Aantal maanden (n): "))

A = (P*r)/(1-(1+r)**(-n))

print(A)