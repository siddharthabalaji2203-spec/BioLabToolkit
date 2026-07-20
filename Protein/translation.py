from Utilities.amino_acid_table import codon_table 

def translation():
    print("==========Translation==========")
    sequence = input("Enter your Sequence:").upper()
    while True:
        if len(sequence) == 0:
            print("Enter a valid Sequence")
            sequence = input("Enter your Sequence:")
        else:
            break
   
    joiner = []
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]
        codon_value = codon_table[codon]
        joiner.append(codon_value)

    final = " - ".join(joiner)
    final = final.replace("\n" ,"")
    print("The Codons present are:" , final)


