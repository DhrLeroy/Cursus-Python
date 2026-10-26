totaal_geheugen_TB = float(input("Geheugen laptop (in TB): "))

geheugen_gebruikt_GB = float(input("Geheugen gebruikt (in GB): "))

geheugen_game_GB = float(input("Grootte van computergame (in GB): "))

totaal_geheugen_GB = totaal_geheugen_TB * 1000

beschikbaar_geheugen_GB = totaal_geheugen_GB - geheugen_gebruikt_GB

if beschikbaar_geheugen_GB < geheugen_game_GB:
    print("Onvoldoende geheugen")