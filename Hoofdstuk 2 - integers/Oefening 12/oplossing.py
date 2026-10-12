aantal = int(input("Hoeveel neem je er? "))

bedrag = (((aantal // 5) * 2) + aantal % 5) * 2.3

print(f'Je moet {round(bedrag,2)} euro betalen.')
