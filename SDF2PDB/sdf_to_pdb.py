#!/usr/bin/env python3

import sys
from rdkit import Chem

# Check that an SDF file path was provided as an argument
if len(sys.argv) != 2:
    print("Usage: python3 sdf_to_pdb.py <sdf_file>")
    sys.exit(1)

sdf_file = sys.argv[1]

# First Load the SDF File Using RDKit
suppl = Chem.SDMolSupplier(sdf_file)

# Check that there is at least one molecule in the SDF file
if suppl is None or len(suppl) == 0:
    print("No molecules found in SDF file: ", sdf_file)
    sys.exit(1)

# Get the first molecule from the SDF file
mol = suppl[0]

# Check that the molecule was loaded successfully
if mol is None:
    print("Could not load molecule from SDF file: ", sdf_file)
    sys.exit(1)

# Write the molecule to a PDB file using RDKit
pdb_file = sdf_file.replace('.sdf', '.pdb')
writer = Chem.PDBWriter(pdb_file)
writer.write(mol)
writer.close()

print("Converted SDF file to PDB file: ", pdb_file)


# How to run script: python3 sdf_to_pdb.py <sdf_file>