from Utilities.dna_mutation_validator import mutationvalidatorreference
from Utilities.dna_mutation_validator import mutationvalidatorsample
def dnamutationfinder():

    #inputs
    sequence_1 = mutationvalidatorreference()
    sequence_2 = mutationvalidatorsample()
    # basic counters to keep track
    i=0
     # to help keep track
    # looping station for substitution mutation (point mutation)
    if len(sequence_1) == len(sequence_2):
        print("---------------")
        print("Mutation Report")
        print("---------------")
        while True:
            for i in range(i,len(sequence_1)):
            
                if sequence_1[i] == sequence_2[i]:
                    i+=1
                    continue
                        
                else:
                
                    print("Position:",i+1)
                    print("Mutatition that has taken place:",sequence_1[i],"-->",sequence_2[i])
                    print("---------------")
                    
            print("Type: Substitution")
            print("Length of the DNA Reference Strand :" , len(sequence_1) ,"bp")
            print("Length of the DNA Sample Strand :" , len(sequence_2) ,"bp")
            print("DNA Sequence Analysis Complete")
            break    
    # deletion mutation
    if len(sequence_1) > len(sequence_2):
        diffrence = len(sequence_1) - len(sequence_2)
        i = len(sequence_2)
        remains = i + diffrence
        print("---------------")
        print("Mutation Report")
        print("---------------")
        print("Reference:",sequence_1)
        print("Sample:", sequence_2)
        print("Type: Deletion")
        print("Nucleotides not found in Sample:" ,sequence_1[i:remains])
        print("Length of the DNA Reference Strand :" , len(sequence_1) ,"bp")
        print("Length of the DNA Sample Strand :" , len(sequence_2) ,"bp")
        print("DNA Sequence Analysis Complete")
    # addition mutation
    if len(sequence_2) > len(sequence_1):
        diffrence = len(sequence_2) - len(sequence_1)
        i = len(sequence_1)
        remains = i + diffrence
        print("---------------")
        print("Mutation Report")
        print("---------------")
        print("Reference:",sequence_1)
        print("Sample:", sequence_2)
        print("Type: Addition")
        print("Nucleotides found in Sample:" ,sequence_2[i:remains])
        print("Length of the DNA Reference Strand :" , len(sequence_1) ,"bp")
        print("Length of the DNA Sample Strand :" , len(sequence_2) ,"bp")
        print("DNA Sequence Analysis Complete")
