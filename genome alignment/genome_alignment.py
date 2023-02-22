#!/usr/bin/env python3

import sys
import subprocess

# Check that two genome FASTA files were provided as arguments
if len(sys.argv) != 3:
    print("Usage: python3 genome_alignment.py <genome1_file> <genome2_file>")
    sys.exit(1)

genome1_file = sys.argv[1]
genome2_file = sys.argv[2]

# Set up the MUMmer command
mummer_cmd = ['nucmer', '--maxmatch', '--prefix=alignment', genome1_file, genome2_file]

# Run MUMmer to perform the genome alignment
subprocess.run(mummer_cmd, check=True)

# Generate the alignment report using show-coords
show_coords_cmd = ['show-coords', '-rcl', 'alignment.delta']
subprocess.run(show_coords_cmd, check=True)
