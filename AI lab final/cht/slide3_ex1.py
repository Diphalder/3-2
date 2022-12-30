seq = input("Enter a DNA sequence: ")
print("It is", len(seq), "bases long")
if("A" in seq):
    print("A count", seq.count("A"))
if("T" in seq):
    print("T count:", seq.count("T"))
if("C" in seq):
    print("C count:", seq.count("C"))
if("G" in seq):
    print("G count:",seq.count("G"))

