from modeller import *

env = environ()
aln = alignment(env)
mdl = model(env, file='5NN8', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='5NN8', atom_files='5NN8.pdb')
aln.append(file='gluc.ali', align_codes='gluc')
aln.align2d()
aln.write(file='alignment.ali', alignment_format='PIR')
aln.write(file='alignment.pap', alignment_format='PAP')
