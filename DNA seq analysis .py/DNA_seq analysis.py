
# Calculate DNA content
print("To calculate DNA content")
dna = input("Enter the sequence of DNA = ").upper()
length = len(dna)

gc_content = (dna.count("G") + dna.count("C")) * 100 / len(dna)
at_content = (dna.count("A") + dna.count("T")) * 100 / len(dna)

print("Length of DNA is =", length)
print("GC content in DNA is =", gc_content, "%")
print("AT content in DNA is =", at_content, "%")


# Counting DNA nucleotides
print("To count DNA nucleotides")
dna = input("Enter the sequence of DNA = ").upper()
length = len(dna)

print("Length of DNA is =", length)
print("A count =", dna.count("A"))
print("T count =", dna.count("T"))
print("G count =", dna.count("G"))
print("C count =", dna.count("C"))


# DNA to RNA
print("DNA to RNA")
dna = input("Enter the sequence of DNA = ").upper()
rna = dna.replace("T", "U")

print("RNA sequence =", rna)


# Composition of DNA
print("Composition of DNA")
dna = input("Enter the sequence of DNA = ").upper()

gc = (dna.count("G") + dna.count("C")) * 100 / len(dna)
at = (dna.count("A") + dna.count("T")) * 100 / len(dna)

if gc >= 50:
    print("GC rich")
    print("GC content =", gc, "%")
else:
    print("AT rich")
    print("AT content =", at, "%")


# REVERSE COMPLEMENT OF DNA SEQUENCE
print("REVERSE COMPLEMENT OF DNA SEQUENCE")
dna = input("Enter the sequence of DNA = ").upper()

complement = {"A": "T", "T": "A", "G": "C", "C": "G"}
comp_seq = "".join(complement[base] for base in dna)
reverse_comp = comp_seq[::-1]
print("Reverse complement =", reverse_comp)
