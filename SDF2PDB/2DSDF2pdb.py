from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw

# load the SDF file
suppl = Chem.SDMolSupplier('input.sdf')

# loop over the molecules and convert to PDB format
for mol in suppl:
    # generate a 3D conformation for the molecule
    AllChem.EmbedMolecule(mol)
    # optimize the conformation
    AllChem.UFFOptimizeMolecule(mol)
    # write the molecule to a PDB file
    writer = Chem.PDBWriter(f'{mol.GetProp("_Name")}.pdb')
    writer.write(mol)
    writer.close()
