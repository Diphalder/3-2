seq = input("Enter a DNA sequence: ")
print("It is", len(seq), "bases long")
if("A" not in seq):
    print("A not found")
elif("T" not in seq):
    print("T not found")
elif("C" not in seq):
    print("C not found")
elif("G" not in seq):
    print("G not found")
elif("A" in seq):
    print("A count", seq.count("A"))
elif("T" in seq):
    print("T count:", seq.count("T"))
elif("C" in seq):
    print("C count:", seq.count("C"))
elif("G" in seq):
    print("G count:",seq.count("G"))