import urllib.request

# 1. RETRIEVE REAL OPEN-SOURCE GENOMIC DATA FROM NCBI
# Fetching the human Insulin (INS) gene sequence in FASTA format
FASTA_URL = "https://nih.gov"

print("[INFO] Fetching open-source genomic sequence from NCBI...")
try:
    with urllib.request.urlopen(FASTA_URL) as response:
        fasta_data = response.read().decode('utf-8')
    print("[SUCCESS] Insulin (INS) gene sequence successfully retrieved.")
except Exception as e:
    print(f"[ERROR] Failed to fetch sequence from NCBI: {e}")
    exit()

# 2. DATA CLEANING & FASTA PARSING
lines = fasta_data.strip().split('\n')
header = lines[0]
# Combine all sequence lines and convert to uppercase for absolute standardization
dna_sequence = "".join(lines[1:]).upper()

print(f"\n--- GENOMIC RECORD METADATA ---")
print(f"Header: {header}")
print(f"Total Sequence Length: {len(dna_sequence)} base pairs (bp)")

# 3. BIOINFORMATICS METRICS PIPELINE
def calculate_gc_content(sequence):
    """Calculates the percentage of Guanine and Cytosine bases."""
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    return ((g_count + c_count) / len(sequence)) * 100

def transcribe_dna_to_rna(sequence):
    """Simulates transcription by replacing Thymine with Uracil."""
    return sequence.replace('T', 'U')

def isolate_potential_codons(sequence):
    """Scans the sequence to locate critical clinical start codons (ATG)."""
    start_codon = "ATG"
    positions = []
    pos = sequence.find(start_codon)
    while pos != -1:
        positions.append(pos)
        pos = sequence.find(start_codon, pos + 1)
    return positions

# 4. RUN EXECUTABLE PIPELINE ANALYSIS
gc_content = calculate_gc_content(dna_sequence)
rna_transcript = transcribe_dna_to_rna(dna_sequence)
start_codon_positions = isolate_potential_codons(dna_sequence)

print("\n--- BIOINFORMATICS ANALYSIS OUTPUT ---")
print(f"GC-Content Ratio: {gc_content:.2f}%")
print(f"RNA Transcript Snapshot (First 60 bp): {rna_transcript[:60]}...")
print(f"Total Start Codons (ATG) Detected: {len(start_codon_positions)}")
print(f"First 5 Start Codon Index Coordinates: {start_codon_positions[:5]}")
print("\n[SUCCESS] Genomics processing complete.")
