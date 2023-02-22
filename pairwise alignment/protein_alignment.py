#!/usr/bin/env python3

import sys
from Bio import pairwise2
from Bio.Seq import Seq
from Bio.SubsMat import MatrixInfo

# Check that two protein sequences were provided as arguments
if len(sys.argv) != 3:
    print("Usage: python3 protein_alignment.py <protein1_sequence> <protein2_sequence>")
    sys.exit(1)

protein1_seq = Seq(sys.argv[1])
protein2_seq = Seq(sys.argv[2])

# Set up the alignment parameters
matrix = MatrixInfo.blosum62
gap_open_penalty = -10.0
gap_extend_penalty = -0.5

# Perform the pairwise sequence alignment
alignments = pairwise2.align.globalds(protein1_seq, protein2_seq, matrix, gap_open_penalty, gap_extend_penalty)

# Print the alignment results
for align in alignments:
    print(pairwise2.format_alignment(*align))
    
# How to run: python3 protein_alignment.py <protein1_sequence> <protein2_sequence>