# Algorithmic DNA Sequence & Bioinformatics Analysis

## Project Objective
This repository hosts a specialized bioinformatics processing script designed to clean, parse, and analyze raw genomic sequences retrieved live from the **National Center for Biotechnology Information (NCBI)** database. The pipeline automatically evaluates critical molecular biomarkers, including total GC-content ratios and transcript translation points on the human insulin (`INS`) gene.

## Technical Architecture & Methods
- **Genomic Automated Integration:** Utilizes web requests to extract real-time FASTA sequences straight from official biological sequence databases.
- **Data Engineering & Standardization:** Automatically removes headers, sanitizes white spaces, and normalizes string casing for character mapping.
- **Bioinformatics String Mapping:** Built native algorithms to calculate programmatic GC-content percentages, simulate DNA-to-RNA transcription steps, and search index arrays to isolate clinical start codon positions (`ATG`).

## Skills Demonstrated
- **Bioinformatics Track:** String manipulation, genomic sequence mapping, and character parsing using pure Python.
- **Relevant DataCamp Track Connection:** Python Data Science Toolbox & Python String Manipulation.

## Setup Instructions
```bash
# Clone this repository
git clone https://github.com

# Run the bioinformatics analysis pipeline
python dna_analysis.py
```
