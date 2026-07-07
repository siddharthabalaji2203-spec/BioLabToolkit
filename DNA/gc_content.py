print("=========GC Content==========")
sequence = input("Enter your Sequence:").upper()
while True:
    if len(sequence) == 0:
        print("Please enter a valid sequence")
        sequence = input("Enter your Sequence:").upper()
    else:
        break
g_counter = 0
c_counter = 0
for base in sequence:
    if base == "C":
        c_counter+=1
    elif base =="G":
        g_counter+=1
gc_count = g_counter + c_counter

gc_count2 = gc_count/len(sequence)

final = gc_count2*100

print("Content of 'C' present:" , c_counter)
print("Content of 'G' present:" , g_counter)
print("GC Content:" , final)
