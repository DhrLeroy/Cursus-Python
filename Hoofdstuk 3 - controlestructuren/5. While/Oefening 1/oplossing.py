while True:
    wachtwoord = input("Oud wachtwoord: ")
    nieuw = input("Nieuw wachtwoord: ")
    herhaling = input("Nieuw wachtwoord (controle): ")

    if wachtwoord != nieuw:
        if nieuw == herhaling:
            break