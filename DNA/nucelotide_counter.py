from Utilities.dna_validator import validator

def nucleotide_counter():
    sequence = validator()
    #banner :)
    print("========== Nucleotide Counter & Percentage Analysis ==========")
    # respective counters
    Adenine = sequence.count("A")
    Thymine = sequence.count("T")
    Guanine = sequence.count("G")
    Cytosine = sequence.count("C")
    # a-t & g-c total contents
    a_t = Adenine + Thymine
    g_c = Guanine + Cytosine
    # length of strand
    length = len(sequence)
    #display of the respective counts
    print("Adenine Count:" , Adenine)
    print("Thymine Count:", Thymine)
    print("Guanine Count:", Guanine)
    print("Cytosine Count:", Cytosine)
    #percentage analysis ( induvidual )
    print("Adenine Percentage:", (Adenine/length)*100)
    print("Thymine Percentage:", (Thymine/length)*100)
    print("Guanine Percentage:", (Guanine/length)*100)
    print("Cytosine Percentage:" ,(Cytosine/length)*100)
    
    #percentage analysis (A-T & G-C)
    print("A-T Percentage:", (a_t/length)*100)
    print("G-C Percentage:", (g_c/length)*100)

    if Adenine + Thymine + Guanine + Cytosine == length:
        print("Length of given sequence:" , length)
        print("Sequence Analysis Complete")
