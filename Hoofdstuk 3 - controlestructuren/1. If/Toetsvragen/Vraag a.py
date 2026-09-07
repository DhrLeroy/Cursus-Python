temperatuur_K = float(input("Temperatuur (in Kelvin): "))
temperatuur_C = temperatuur_K - 273

if temperatuur_C <= 0:
    print(f"{temperatuur_C}°C: Vast (ijs)")
if 0 < temperatuur_C < 100:
    print(f"{temperatuur_C}°C: Vloeibaar (water)")
if temperatuur_C >= 100:
    print(f"{temperatuur_C}°C: Gas (waterdamp)")
