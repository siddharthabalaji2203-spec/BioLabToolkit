def fasta_reader():
    with open("Data/sample.fasta", "r") as file:
        lines = file.readlines()

    header = lines[0].replace(">", "").strip()

    sequence_lines = lines[1:]

    sequence = "".join(sequence_lines)

    sequence = sequence.replace("\n", "")

    length = len(sequence)

    print("========== FASTA READER ==========")
    print()
    print("Header:", header)
    print()
    print("Sequence:", sequence)
    print()
    print("Length:", length, "bp")

    print("Sequence Analysis Complete")
