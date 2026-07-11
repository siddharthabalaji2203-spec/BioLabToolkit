#reference
def mutationvalidatorreference():
    while True:
        sequence_1 = input("Enter your DNA Reference Sequence:").upper().strip()
        
        nucleotides = ["A","T","G","C"]
        valid_1 = True
        if not sequence_1:
            print("Sequence cannot be empty.")
            continue
        for letter in sequence_1:
            if letter not in nucleotides:
                valid = False
                break
        if valid_1:
            return sequence_1
            
        else:
            print("The provided sequence is not a DNA sequence")
            print("Provide a valid DNA sequence")
# sample

def mutationvalidatorsample():
    while True:
        sequence_2 = input("Enter your DNA Sample Sequence:").upper().strip()
        nucleotides = ["A","T","G","C"]
        valid_2 = True
        if not sequence_2:
            print("Sequence cannot be empty.")
            continue
        for letter in sequence_2:
            if letter not in nucleotides:
                valid = False
                break
        if valid_2:
            return sequence_2
            
        else:
            print("The provided sequence is not a DNA sequence")
            print("Provide a valid DNA sequence")
