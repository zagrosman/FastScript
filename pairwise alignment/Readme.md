# Compare two protein sequences

To conduct a pairwise alignment on two protein sequences, you can use this script. The script uses the `pairwise2` module from Biopython to perform a global pairwise sequence alignment of the two protein sequences. The BLOSUM62 substitution matrix is used to score matches and mismatches, and the gap open and extension penalties are set to -10 and -0.5, respectively. The script then prints the alignment results to the console.

# How to run
To use the script, save it as `protein_alignment.py` and run it from the command line with the two protein sequences as arguments:

```
python3 protein_alignment.py <protein1_sequence> <protein2_sequence>
```
