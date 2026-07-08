def validator():
    while True:
        sequence = input("Enter your DNA Sequence:").upper().strip()
        nucleotides = ["A","U","G","C"]
        valid = True
        if not sequence:
            print("Sequence cannot be empty.")
            continue
        for letter in sequence:
            if letter not in nucleotides:
                valid = False
                break
        if valid:
            return sequence
            
        else:
            print("The provided sequence is not a DNA sequence")
            print("Provide a valid DNA sequence")

