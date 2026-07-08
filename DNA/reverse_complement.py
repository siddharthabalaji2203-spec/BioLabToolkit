from Utilities.dna_validator import validator

def reverse_complement():
    print("==========Reverse Complement Generator==========")
    sequence = validator()
    while True:
        if len(sequence) == 0:
            print("Please enter a valid sequence")
            sequence = input("Enter your Sequence:").upper()
        else:
            break
    base_complement = { "A":"T",
                        "G":"C" ,
                        "T":"A" ,
                        "C":"G" }
    compliment = []

    for base in sequence :
        complement = (base_complement[base])
        compliment.append(complement)


    final = "".join(compliment)
    final = final.replace("\n","")
    rev_final = final[::-1]

    print("Reverse Complementary Strand:" , rev_final)


