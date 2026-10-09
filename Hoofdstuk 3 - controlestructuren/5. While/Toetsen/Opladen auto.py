lading = float(input("Huidige lading (kWh): "))
max_capaciteit = float(input("Maximale capaciteit (kWh): "))

gewenst_lading = max_capaciteit*0.995

tijd = 0

while lading < gewenst_lading:
    ontbrekend = max_capaciteit - lading
    lading = lading + ontbrekend * 0.025
    
    tijd += 1

print(f"Na {tijd//60} uur en {tijd%60} minuten werd de gewenste lading bereikt.")