# SDF2PDB python script

Using this script, you can convert SDF format to PDB format. Please not that this script uses [RDkit](https://www.rdkit.org/) to conduct the stuctural conversion. You can use [this file](https://github.com/zagrosman/FastScript/blob/master/SDF2PDB/quercetin.sdf) to run the script. Please use PubChem or other chemical databases to download SDF files. 


# How to run SDF2PDB script?

Simply run the following command:

```
python3 sdf_to_pdb.py <sdf_file>

```

or 

```
python sdf_to_pdb.py <sdf_file>

```


# How to run 2DSDF2pdb.py

You can run it using the previous commands. Please note that this script accepts 2D sdf files instead of 3D sdf files and the written codes have been modified a little bit. Please check [this file](https://github.com/zagrosman/FastScript/blob/master/SDF2PDB/2DSDF2pdb.py) to run this script. 
<p align="justify">In this script, we first open the 2D SDF file using Chem.SDMolSupplier. We then loop over the molecules in the file, generate a 3D conformation for each molecule using AllChem.EmbedMolecule, optimize the conformation using AllChem.UFFOptimizeMolecule, and write the molecule to a PDB file using Chem.PDBWriter. The name of each PDB file is set to the name of the molecule using the _Name property.</p>


# How to run 3dsdf2pdb.js?

This is a java script. In this script, we first get the input SDF file name from the command line argument `(args[0])`. We then use `String.replace` to replace the `".sdf" extension` with `".pdb"` to get the output PDB file name. We then use `FileInputStream` and `MDLV2000Reader` from the CDK library to read the input SDF file and convert it into an `IAtomContainer` object. We then use `FileOutputStream` and `PDBWriter` from the CDK library to write the `IAtomContainer` object to the output PDB file.


