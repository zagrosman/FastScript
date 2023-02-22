# Pairwise genome alignment

The script uses the nucmer command from the MUMmer package to perform a pairwise alignment of the two bacterial genomes. The --maxmatch option is used to maximize the number of exact matches, and the --prefix option is used to specify the prefix for the output files. The resulting alignment is saved in the alignment.delta file. The script then uses the show-coords command from MUMmer to generate a report of the alignment results in a tabular format, which is printed to the console.

# How to run

```
python3 genome_alignment.py <genome1_file> <genome2_file>
```
