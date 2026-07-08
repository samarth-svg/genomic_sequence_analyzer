# genomic_sequence_analyzer
pure-Python bioinformatics tool for parsing FASTA files and analyzing GC-content to evaluate genetic stability.

  Genomic Sequence Analyzer & GC-Content Parser 

A pure-Python bioinformatics pipeline designed to parse genomic data in the standard FASTA format and calculate key sequence metrics, specifically Guanine-Cytosine (GC) content. 

This tool was developed to bridge the gap between computational data and applied biology, with applications ranging from evaluating thermodynamic stability of DNA to understanding viral immune evasion strategies.

## Scientific Context
Calculating GC content is a foundational step in genetic analysis with significant clinical and biological applications:
* **Virology:** Analyzing GC bias between viral genomes and host mammalian genes reveals evolutionary adaptations and mechanisms of host immune evasion.
* **Molecular Diagnostics:** GC content dictates the melting temperature (Tm) of DNA sequences, which is an essential parameter for designing highly specific PCR primers.
* **Epigenetics:** Gene-dense regions frequently correlate with GC-rich domains, and the methylation state of "CpG islands" dictates gene silencing or activation.

## Features
* **Zero Dependencies:** Built entirely using Python's standard library. No external packages required.
* **Memory Efficient:** Processes FASTA files sequentially to handle large genomes.
* **Automated Sample Generation:** Includes a built-in function to generate a dummy FASTA file with accurate nucleotide ratios for testing.

## Quick Start
1. Clone the repository or download the files.
2. Open your terminal and navigate to the project directory.
3. Run the script:
   ```bash
   python3 sequence_analyzer.py
