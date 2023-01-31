def DNA_strand(dna: str) -> str:
    complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return "".join(complements[base] for base in dna)