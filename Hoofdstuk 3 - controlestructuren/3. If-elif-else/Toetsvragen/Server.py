temperatuur_C = float(input("Geef de temperatuur van het serverlokaal (in °C): "))

if temperatuur_C < 18:
    extra = 18 - temperatuur_C
    print(f"Te koud: energieverlies door overkoeling. Verhoog de temperatuur met {extra} °C.")
elif temperatuur_C > 35:
    print("Kritieke temperatuur! Risico op oververhitting.")
elif temperatuur_C > 27:
    extra = temperatuur_C - 27
    print(f"Waarschuwing: serverlokaal warm. Verlaag temperatuur met {extra} °C.")
else:
    print("Temperatuur is optimaal.")