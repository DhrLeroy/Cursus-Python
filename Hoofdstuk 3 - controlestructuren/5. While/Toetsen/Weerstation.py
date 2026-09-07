gemiddelde = 0
dag = 0

while True:
    dag = dag + 1
    hoogste_invoer = input(f"Temperatuur (in °C) voor dag {dag} (hoogste temperatuur): ")
    if hoogste_invoer == "STOP":
        dag = dag - 1
        break
    hoogste_C = float(hoogste_invoer)
    laagste_C = float(input(f"Temperatuur (in °C) voor dag {dag} (laagste temperatuur): "))
    gemiddelde = gemiddelde + (hoogste_C + laagste_C)/2

gemiddelde = gemiddelde / dag

print(f"Weeroverzicht voor de afgelopen {dag} dagen:")
print(f"Gemiddelde temperatuur: {gemiddelde} °C")