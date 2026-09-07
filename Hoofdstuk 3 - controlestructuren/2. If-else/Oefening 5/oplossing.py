breedte_cm = float(input("Breedte van de bagage (in cm)? "))
hoogte_cm = float(input("Hoogte van de bagage (in cm)? "))
diepte_cm = float(input("Diepte van de bagage (in cm)? "))

volume_dm3 = breedte_cm*hoogte_cm*diepte_cm/1000

if volume_dm3 > 80:
    print("Geen check-in")
else:
    soort_ticket = input("Welk soort ticket (business/economy) hebt u? ")
    if soort_ticket == "Economy":
        gewicht_kg = float(input("Hoeveel weegt de bagage (in kg)? "))
        if gewicht_kg > 20:
            print("Check-in mits bijpassing")
        else:
            print("Check-in")
    else:
        if soort_ticket == "Business":
            print("Check-in")
        else:
            print("Ongeldig ticket")