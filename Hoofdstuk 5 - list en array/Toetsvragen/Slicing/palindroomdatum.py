geboortedatum = input("Geef jouw geboortedatum (dd/mm/jjjj): ")
geboortedatum_cijfers = geboortedatum[0:2]+geboortedatum[3:5]+geboortedatum[6:]

wel_niet = "een" if geboortedatum_cijfers == geboortedatum_cijfers[::-1] else "geen"
print(f"{geboortedatum} is {wel_niet} palindroomdatum.")