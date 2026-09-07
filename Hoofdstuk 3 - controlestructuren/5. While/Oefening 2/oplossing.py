jaar = int(input("Jaar: "))
maand = int(input("Maand: "))

schikkeljaar = False
if jaar % 4 == 0:
    if jaar % 100 != 0:
        schikkeljaar = True
if jaar % 400 == 100:
    schikkeljaar = True

while True:
    dag = int(input("Dag: "))
    if dag < 1:
        continue
    if maand == 1:
        if dag <= 31:
            break
    elif maand == 2:
        if schikkeljaar:
            if dag <= 29:
                break
        else:
            if dag <= 28:
                break
    elif maand == 3:
        if dag <= 31:
            break
    elif maand == 4:
        if dag <= 30:
            break
    elif maand == 5:
        if dag <= 31:
            break
    elif maand == 6:
        if dag <= 30:
            break
    elif maand == 7:
        if dag <= 31:
            break
    elif maand == 8:
        if dag <= 31:
            break
    elif maand == 9:
        if dag <= 30:
            break
    elif maand == 10:
        if dag <= 31:
            break
    elif maand == 11:
        if dag <= 30:
            break
    elif maand == 12:
        if dag <= 31:
            break