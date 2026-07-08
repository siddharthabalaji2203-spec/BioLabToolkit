from Utilities.dna_validator import validator

def complement():
    print("==========Complement Generator==========")
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

    prefinal = compliment[0:]
    final = "".join(prefinal)
    final = final.replace("\n","")

    print("Complementary Strand:" , final)
    
