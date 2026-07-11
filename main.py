from DNA.complement import complement
from DNA.fasta_reader import fasta_reader
from DNA.gc_content import gc_content
from DNA.reverse_complement import reverse_complement
from DNA.nucelotide_counter import nucleotide_counter
from DNA.dna_mutation_detector import dnamutationfinder
from RNA.transcription import transcription
from Protein.translation import translation


# Menu display and tool mapping


def display_menu():
    """Print the main menu with all available tools."""
    print("\n========== BioLabToolkit ==========")
    print("Welcome to BioLabToolkit")
    print("Tools Available:")
    print("DNA:")
    print("  1) FASTA Reader")
    print("  2) GC Content Calculator")
    print("  3) Complement Strand Synthesis")
    print("  4) Reverse Complement Strand Synthesis")
    print("  5) Nucleotide Counter with Percentage Analysis")
    print("  6) DNA Mutation Analysis")
    print("RNA:")
    print("  7) Transcription")
    print("Protein:")
    print("  8) Translation")
    print("------------------------------------")
    print("Type the name or number of the tool, or 'quit' to exit.")


TOOL_MAP = {
    # Numbers as strings
    "1": fasta_reader,
    "2": gc_content,
    "3": complement,
    "4": reverse_complement,
    "5": nucleotide_counter,
    "6": dnamutationfinder,
    "7": transcription,
    "8":translation,
    # Full names (lowercase for matching)
    "fasta reader": fasta_reader,
    "gc content calculator": gc_content,
    "complement strand synthesis": complement,
    "reverse complement strand synthesis": reverse_complement,
    "transcription": transcription,
    "translation": translation,
    "nucleotide counter": nucleotide_counter,
    "dna mutation finder": dnamutationfinder
}


# Main program logic


def run_tool(choice):
    """
    Look up the chosen tool in the map and execute it.
    Returns True if a valid tool was found and run, False otherwise.
    """
    # Normalize input: strip spaces and convert to lowercase for name matching
    key = choice.strip().lower()
    
    # If the key is not directly in the map, try matching as a number (already strings)
    if key not in TOOL_MAP:
        print("Tool not found. Please check your spelling or number.")
        print("Kindly wait for future updates if the tool isn't listed.")
        return False
    
    # Execute the corresponding function
    tool_func = TOOL_MAP[key]
    tool_func()
    return True

def main():
    """Main loop: display menu, get input, run tool, repeat until user quits."""
    while True:
        display_menu()
        user_input = input("Please select the tool you want to run: ").strip()
        
        # Exit condition
        if user_input.lower() in ("quit", "exit", "q"):
            print("Thanks for using BioLabToolkit!")
            break
        
        # If input is empty, prompt again (but the loop will re-display menu)
        if not user_input:
            print("Input cannot be empty. Please try again.")
            continue
        
        # Run the selected tool
        success = run_tool(user_input)
        
        if success:
            # Ask if the user wants to continue or exit
            while True:
                again = input("\nWould you like to use another tool? (yes/no): ").strip().lower()
                if again in ("yes", "y"):
                    break   # exit inner loop, go back to main menu
                elif again in ("no", "n"):
                    print("Thanks for using BioLabToolkit!")
                    return  # exit the entire program
                else:
                    print("Please answer 'yes' or 'no'.")
        # If tool not found, the loop continues to the main menu automatically


# Entry point

if __name__ == "__main__":
    main()
    
