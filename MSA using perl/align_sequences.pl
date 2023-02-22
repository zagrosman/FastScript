#!/usr/bin/perl

use strict;
use warnings;

# Check that a set of FASTA files was provided as arguments
if (@ARGV < 2) {
    print "Usage: perl align_sequences.pl <sequence1.fasta> <sequence2.fasta> ... <sequenceN.fasta>\n";
    exit 1;
}

# Set up the ClustalW command
my $clustalw_exe = '/path/to/clustalw';  # Replace with the path to the ClustalW executable
my $input_files = join(' ', @ARGV);
my $output_file = 'alignment.aln';
my $clustalw_cmd = "$clustalw_exe $input_files -outfile=$output_file";

# Run ClustalW to perform the multiple sequence alignment
system($clustalw_cmd) == 0 or die "Error running ClustalW: $!";

print "Multiple sequence alignment complete. Results saved to $output_file\n";
