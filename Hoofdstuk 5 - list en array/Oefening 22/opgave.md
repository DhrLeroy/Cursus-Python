22.	Een IBAN-rekeningnummer bestaat uit een landcode (bv. BE), gevolgd door 2 cijfers (controlegetal) en vervolgens 3 keer 4 cijfers (rekeningnummer). Bijvoorbeeld: BE68 5390 0754 7034.
Het controlegetal zorgt ervoor dat de volgende wiskundige berekening klopt. Typ je dus een verkeerd cijfer in als IBAN-rekeningnummer, dan is het volledige rekeningnummer incorrect en zal een overschrijving bijvoorbeeld niet gebeuren.
De wiskundige berekening:
1)	Plaats alle delen aan elkaar (dus zonder spaties)
Bv.: BE68539007547034
2)	Verplaats de eerste 4 tekens naar achter.
Bv.: 539007547034BE68
3)	Vervang de letters van de landcode door cijfers. Een A wordt een 10, een B wordt een 11, een C wordt een 12, etc. Je hoeft dit enkel van A-E uit te werken voor deze oefening.
Bv.: 539007547034111468
4)	Als je vervolgens de rest na de deling van dit getal door 97 neemt, moet je een 1 uitkomen. Dan is dit een geldig rekeningnummer.
Bv.: rest na deling van 539007547034111468 door 97 = 1. Dit is dus een geldig rekeningnummer.
Maak een programma waarbij je het IBAN-rekeningnummer (met spaties) bevraagd aan de gebruiker. Toon vervolgens of dit een geldig rekeningnummer is.
Voorbeeld:
Geef het IBAN-rekeningnummer in: BE68 5390 0754 7034
BE68 5390 0754 7034 is een geldig rekeningnummer.
Geef het IBAN-rekeningnummer in: BE10 2345 7890 1234
BE10 2345 7890 1234 is geen geldig rekeningnummer.
