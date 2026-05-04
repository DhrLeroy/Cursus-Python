while True:

    K = float(input("Temperatuur (in Kelvin): "))
    C = K - 273

    if C <= 0:
        print(f"{C}°C: Vast (ijs)")
    if 0 < C < 100:
        print(f"{C}°C: Vloeibaar (water)")
    if C >= 100:
        print(f"{C}°C: Gas (waterdamp)")
