dna = input("Geef een DNA-fragment in: ")

stopcodons = ["TAA", "TAG", "TGA"]
genen = []

for start in range(len(dna) - 2):

    if dna[start:start + 3] == "ATG":

        for einde in range(start + 3, len(dna) - 2, 3):

            codon = dna[einde:einde + 3]

            if codon in stopcodons:

                gen = dna[start:einde + 3]

                if len(gen) % 3 == 0:
                    genen.append(gen)

                break

print("Gevonden coderende DNA-sequenties:")
print(genen)

print()
print(f"Aantal coderende DNA-sequenties: {len(genen)}")

if len(genen) > 0:

    langste = genen[0]

    for gen in genen:
        if len(gen) > len(langste):
            langste = gen

    aantal_codons = len(langste) // 3

    print(f"Langste coderende DNA-sequentie: {langste}")
    print(f"Aantal codons: {aantal_codons}")

else:
    print("Geen coderende DNA-sequenties gevonden.")