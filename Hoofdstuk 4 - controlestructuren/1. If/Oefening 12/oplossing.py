diepte = float(input("Diepte (in meter): "))

zwaartekracht_aarde = 9.81
dichtheid_water = 1000

hydrostatische_druk_Pa = dichtheid_water * zwaartekracht_aarde * diepte

luchtdruk_bar = 1.013

hydrostatische_druk_bar = hydrostatische_druk_Pa / 100000

totale_druk_bar = luchtdruk_bar + hydrostatische_druk_bar

if totale_druk_bar <= 3:
    print('De druk op de tank is nu nog veilig')
if totale_druk_bar > 3:
    print('Druk op de tank (berekende totale druk) is te hoog!')