# How to show Hydrogen bonds in Pymol

1. Install [PyMOL](https://pymol.org/2/)
2. Load the receptor and ligand PDB files using the `load` command and assign them to objects called "receptor" and "ligand", respectively.
3. Create a selection for the receptor-ligand interface using the interface_residues command with a cutoff of 4.0 angstroms. This will select all residues within 4 angstroms of any atom in the other molecule.
4. Use the find_pairs command to find all hydrogen bonds between the interface residues of the receptor and the ligand. This command takes four arguments: the selection of atoms to consider (in this case, the interface residues), the type of bond to look for ('hydrogen' in this case), the role of the selected atoms in the bond ('donor' for the receptor and 'acceptor' for the ligand), and the maximum distance between the donor and acceptor atoms.
5. Print out the hydrogen bonds using a for loop and the print command.
6. Color the hydrogen bonds in green using the color command.



# How to run script_name.py?
You can run this script in PyMOL by saving it as a text file with a ".py" extension and then running the command run `H-bonds.py` in the PyMOL command line. Be sure to replace "receptor.pdb" and "ligand.pdb" with the actual names of your receptor and ligand PDB files.
