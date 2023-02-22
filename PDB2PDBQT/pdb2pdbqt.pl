#!/usr/bin/perl
use strict;
use warnings;
use File::Basename;

# Input file
my $pdb_file = $ARGV[0];

# Output file
my $pdbqt_file = basename($pdb_file, ".pdb") . ".pdbqt";

# Run AutoDockTools to convert PDB to PDBQT
system("pythonsh", "/path/to/mgltools_xxx/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_ligand4.py",
       "-l", $pdb_file,
       "-o", $pdbqt_file,
       "-U", "nphs",
       "-A", "hydrogens",
       "-s", "both",
       "-B", "residues");

# Check if the output file was generated
if (-e $pdbqt_file) {
    print "Conversion successful. Output file: $pdbqt_file\n";
} else {
    die "Conversion failed. Output file not generated.\n";
}
