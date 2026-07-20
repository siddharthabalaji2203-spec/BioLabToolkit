def fasta_reader():
    # Use a dictionary to store header:sequence pairs
    fasta_dict = {}
    current_header = None

    with open("Data/sample.fasta", "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue  # Skip empty lines
            
            if line.startswith(">"):
                # Track the new gene header
                current_header = line.replace(">", "")
                fasta_dict[current_header] = []
            else:
                # Append sequence lines to the active gene
                if current_header:
                    fasta_dict[current_header].append(line)

    print("========== FASTA READER ==========\n")
    
    # Loop through and print every gene found
    for header, seq_list in fasta_dict.items():
        sequence = "".join(seq_list)
        length = len(sequence)
        
        print(f"Header: {header}")
        print(f"Sequence: {sequence}")
        print(f"Length: {length} bp")
        print("-" * 34)

    print("\nSequence Analysis Complete")
