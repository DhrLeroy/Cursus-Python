concentratie_mol_L = float(input("Geef de beginconcentratie (in mol/L): "))
eindconcentratie_mol_L = float(input("Geef de eindconcentratie (in mol/L): "))

grens_concentratie_mol_L = eindconcentratie_mol_L * 1.02
# of volgens voorbeeld van de opgave
# grens_concentratie_mol_L = eindconcentratie_mol_L + (concentratie_mol_L-eindconcentratie_mol_L)*0.02
minuten = 0

while concentratie_mol_L > grens_concentratie_mol_L:
    minuten = minuten + 1
    concentratie_mol_L = concentratie_mol_L - (concentratie_mol_L - eindconcentratie_mol_L)*0.04

print(f"De reactie bereikte 2% restverschil na {minuten} minuten.")
print(f"Concentratie op dat moment: {concentratie_mol_L} mol/L.")