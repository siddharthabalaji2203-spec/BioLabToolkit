def reverse_complement():
    print("==========Complement Generator==========")
    sequence = input("Enter your Sequence:").upper()
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

    print("Complementary Strand:" , rev_final)

