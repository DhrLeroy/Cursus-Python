zin = input("Zin: ") + " "
begin = 0
zin_omgedraaid = ""
for positie in range(len(zin)):
    if zin[positie] == " " or positie == len(zin)-1:
        woord_omgedraaid = ""
        if begin == 0:
            woord_omgedraaid = zin[positie::-1]
        else:
            woord_omgedraaid = zin[positie:begin:-1]
        begin = positie
        zin_omgedraaid = zin_omgedraaid+woord_omgedraaid
print(zin_omgedraaid)