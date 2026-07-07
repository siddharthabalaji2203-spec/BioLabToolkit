print("==========Transcription==========")
sequence = input("Enter your Sequence:").upper()
while True:
    if len(sequence) == 0:
        print("Please enter a valid sequence")
        sequence = input("Enter your Sequence:").upper()
    else:
        break
base_complement = { "A":"A",
                    "G":"G" ,
                    "T":"U" ,
                    "C":"C"}
compliment = []
for base in sequence :
    complement = (base_complement[base])
    compliment.append(complement)

final = "".join(compliment)
final = final.replace("\n","")

print("Transcription Strand:" , final)

