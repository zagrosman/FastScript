# Multiple sequence alignment using Perl

To use the script, save it as `align_sequences.pl` and run it from the command line with the paths to the input FASTA files as arguments:

```
perl align_sequences.pl <sequence1.fasta> <sequence2.fasta> ... <sequenceN.fasta>
```

The script uses the ClustalW program to perform the multiple sequence alignment. The input FASTA files are passed to ClustalW as a space-separated list, and the output file is specified using the -outfile option. The resulting alignment is saved in the alignment.aln file. The script then prints a message indicating the alignment is complete and where to find the output file.
