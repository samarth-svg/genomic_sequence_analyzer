#!/usr/bin/env python3
"""
Stock Python Genomic Sequence Parser and GC-Content Analyzer
No external dependencies required (Pure Python).
"""

import sys
import os

def create_sample_data(filepath):
    """Generates a dummy FASTA file to match the expected output parameters."""
    print(f"Generating sample data at {filepath}...")
    
    # Sequence 1 (NC_045512.2): 29903 bp, 37.97% GC -> ~11354 G/C, 18549 A/T
    seq1 = ('G' * 5677) + ('C' * 5677) + ('A' * 9275) + ('T' * 9274)
    
    # Sequence 2 (NM_002046.7): 1521 bp, 54.31% GC -> ~826 G/C, 695 A/T
    seq2 = ('G' * 413) + ('C' * 413) + ('A' * 348) + ('T' * 347)
    
    with open(filepath, 'w') as f:
        f.write(">NC_045512.2 Severe acute respiratory syndrome coronavirus 2\n")
        # Write in chunks of 80 characters (standard FASTA format)
        for i in range(0, len(seq1), 80):
            f.write(seq1[i:i+80] + "\n")
            
        f.write(">NM_002046.7 Homo sapiens GAPDH transcript variant 1\n")
        for i in range(0, len(seq2), 80):
            f.write(seq2[i:i+80] + "\n")

def parse_fasta(filepath):
    """Reads a FASTA file and returns a list of (id, sequence) tuples."""
    sequences = []
    current_id = None
    current_seq_chunks = []

    try:
        with open(filepath, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                if line.startswith(">"):
                    if current_id is not None:
                        # Join the accumulated sequence chunks
                        sequences.append((current_id, "".join(current_seq_chunks)))
                    # Extract the ID (the first word after '>')
                    current_id = line[1:].split()[0] 
                    current_seq_chunks = []
                else:
                    # Accumulate sequence data
                    current_seq_chunks.append(line.upper())
            
            # Catch the final sequence in the file
            if current_id is not None:
                sequences.append((current_id, "".join(current_seq_chunks)))
                
    except Exception as e:
        print(f"An error occurred reading the file: {e}", file=sys.stderr)
        sys.exit(1)
        
    return sequences

def analyze_sequences(sequences):
    """Calculates length and GC content for raw sequences."""
    metrics = []
    for seq_id, seq_data in sequences:
        seq_length = len(seq_data)
        
        if seq_length == 0:
            gc_percent = 0.0
        else:
            # Count G and C bases
            g_count = seq_data.count('G')
            c_count = seq_data.count('C')
            gc_percent = ((g_count + c_count) / seq_length) * 100
            
        metrics.append({
            "ID": seq_id,
            "Length": seq_length,
            "GC_Content": round(gc_percent, 2)
        })
    return metrics

def print_report(metrics):
    """Prints the formatted output table to the console."""
    print("-" * 60)
    print(f"{'Sequence ID':<25} | {'Length (bp)':<15} | {'GC Content (%)':<15}")
    print("-" * 60)
    
    for item in metrics:
        # Truncate IDs longer than 24 chars to keep the table clean
        print(f"{item['ID'][:24]:<25} | {str(item['Length']):<15} | {str(item['GC_Content']):<15}")
    print("-" * 60)

if __name__ == "__main__":
    sample_file = "sample_data.fasta"
    
    # 1. Create the dummy fasta file if it doesn't exist
    if not os.path.exists(sample_file):
        create_sample_data(sample_file)
        
    # 2. Parse the pure standard library way
    print(f"Analyzing {sample_file}...\n")
    raw_sequences = parse_fasta(sample_file)
    
    # 3. Calculate metrics and print
    if raw_sequences:
        calculated_metrics = analyze_sequences(raw_sequences)
        print_report(calculated_metrics)
    else:
        print("No sequence data found.")