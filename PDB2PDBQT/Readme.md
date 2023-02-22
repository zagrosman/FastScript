# How to convert pdb2pdbqt file?

You can use this script to convert your pdb files into docking pdbqt inputs. First, you should install **mgltools and ADT** on your system. After installation, add the mgltools path to the script. 

In this script, we first get the input PDB file from the command line argument ($ARGV[0]). We then use File::Basename to get the base name of the input file and append ".pdbqt" to it to get the output file name. We then use system to run prepare_ligand4.py from AutoDockTools to convert the PDB to PDBQT, with the following options:

-l : input PDB file
-o : output PDBQT file
-U nphs : remove non-polar hydrogens
-A hydrogens : add polar hydrogens
-s both : generate PDBQT for both ligand and protein
-B residues : define the binding site residues automatically
After the conversion is complete, we check if the output file was generated using -e and print a success message if it was generated, or die with an error message if it wasn't generated.
