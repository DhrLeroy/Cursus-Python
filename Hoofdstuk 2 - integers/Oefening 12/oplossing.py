aantal = int(input("Hoeveel neem je er? "))

aantal_stuks_in_promo = 2+3

aantal_promos = aantal // aantal_stuks_in_promo

aantal_buiten_promo = aantal % aantal_stuks_in_promo

bedrag = (aantal_promos * 2 + aantal_buiten_promo) * 2.3

print(f'Je moet {round(bedrag,2)} euro betalen.')
