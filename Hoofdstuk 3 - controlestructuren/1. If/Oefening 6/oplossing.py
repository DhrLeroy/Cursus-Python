rpm = int(input("RPM: "))

if rpm > 2000:
    extraRPM = rpm - 2000

    minuten_70graden = ((70-15)/(extraRPM*0.02))/60
    if minuten_70graden < 60:
        print(f"Snelheid verlagen! (minuut {minuten_70graden//1})")
    
    minuten_90graden = ((90-15)/(extraRPM*0.02))/60
    if minuten_90graden < 60:
        print(f"Oververhitting, schakel nu de motor uit! (minuut {minuten_90graden//1})")
