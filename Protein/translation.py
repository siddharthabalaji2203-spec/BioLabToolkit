print("==========Translation==========")
sequence = input("Enter your Sequence:")
while True:
    if len(sequence) == 0:
        print("Enter a valid Sequence")
        sequence = input("Enter your Sequence:")
    else:
        break
codon_table = {
    "AUG": "Methionine or Start",
    "GCU": "Alanine",
    "GCC": "Alanine",
    "GCA": "Alanine",
    "GCG": "Alanine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine"
}
joiner = []
for i in range(0, len(sequence), 3):
    codon = sequence[i:i+3]
    codon_value = codon_table[codon]
    joiner.append(codon_value)

final = " , ".join(joiner)
final = final.replace("\n" ,"")
print("The Codons present are:" , final)
