metingen = [-6.1, -5.9, -6.3, -3.4, -2.9, -1.7, 0, 3.7, 5.6, 4.9]

laagste = metingen[0]
hoogste = metingen[0]

for meting in metingen:
    if meting < laagste:
        laagste = meting
    if meting > hoogste:
        hoogste = meting

print(f'Hoogst gemeten temperatuur: {hoogste}°C')
print(f'Laagst gemeten temperatuur: {laagste}°C')