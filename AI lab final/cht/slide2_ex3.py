restriction_sites = [
  "GAATTC",    # EcoRI
  "GGATCC",    # BamHI
  "AAGCTT",    # HindIII
]


str = input("Enter a sequence: ")
for i  in range(len(restriction_sites)):
    print(restriction_sites[i], "is in the sequence")