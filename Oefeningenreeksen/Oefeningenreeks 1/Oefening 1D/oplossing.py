import sys

getal = int(input("Getal: "))

reeks = []

while getal < 1000:
    reeks.append(getal)
    diff_starting_digit = getal % 10
    #next = next_starting_digit * (10*(len(str(getal))-1)) + round(getal,-1)
    diff_ending_digit_1 = int(str(getal)[len(str(getal))-2])+diff_starting_digit
    diff_ending_digit_2 = diff_ending_digit_1 + 1

    diff1 = int(str(diff_starting_digit)+str(diff_ending_digit_1))
    if str(x1)[0] == diff_ending_digit_1:
        getal = x1
        continue
    diff2 = int(str(diff_starting_digit)+str(diff_ending_digit_2))
    x2 = getal + diff2
    if str(getal + diff2)[0] == diff_ending_digit_2:
        getal = x2
        continue
    getal = sys.maxsize

print(reeks)
