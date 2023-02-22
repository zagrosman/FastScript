import org.openscience.cdk.DefaultChemObjectBuilder;
import org.openscience.cdk.interfaces.IAtomContainer;
import org.openscience.cdk.io.MDLV2000Reader;
import org.openscience.cdk.io.PDBWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;

public class SDFtoPDBConverter {

    public static void main(String[] args) throws Exception {
        // Input SDF file
        String sdfFile = args[0];
        
        // Output PDB file
        String pdbFile = sdfFile.replace(".sdf", ".pdb");
        
        // Read the input SDF file
        FileInputStream fis = new FileInputStream(new File(sdfFile));
        MDLV2000Reader reader = new MDLV2000Reader(fis);
        IAtomContainer molecule = reader.read(DefaultChemObjectBuilder.getInstance().newInstance(IAtomContainer.class));
        reader.close();
        
        // Write the molecule to a PDB file
        FileOutputStream fos = new FileOutputStream(new File(pdbFile));
        PDBWriter writer = new PDBWriter(fos);
        writer.writeMolecule(molecule);
        writer.close();
    }
}
