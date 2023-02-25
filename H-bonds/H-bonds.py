# Load receptor and ligand PDB files
load receptor.pdb, receptor
load ligand.pdb, ligand

# Create a selection for the receptor-ligand interface
interface = interface_residues(receptor, ligand, cutoff=4.0)

# Find hydrogen bonds between the interface residues of the receptor and the ligand
hbonds = find_pairs(interface, 'hydrogen', 'donor', 'acceptor')

# Print out the hydrogen bonds
print("Hydrogen bonds:")
for bond in hbonds:
    print(bond)
    
# Color the hydrogen bonds in green
color green, hbonds
