import os
from invcryrep.invcryrep import InvCryRep
from pymatgen.core.structure import Structure
from pymatgen.analysis.structure_matcher import StructureMatcher, ElementComparator
os.environ["XTB_MOD_PATH"] = "/crystal/xtb_noring_nooutput_nostdout_noCN"
# obtaining the pymatgen Structure instance of Sr3Ru2O7
original_structure = Structure.from_file(filename='Sr3Ru2O7.cif')
# creating an instance of the InvCryRep Class (initialization)
backend=InvCryRep(graph_method='econnn')
# converting a crystal structure to its SLICES string and perform data augmentation (2000x)
slices_list=backend.structure2SLICESAug(original_structure,3,2000) 
slices_list_unique=list(set(slices_list))
cannon_slices_list=[]
for i in slices_list_unique:
    cannon_slices_list.append(backend.get_canonical_SLICES(i))
# test get_canonical_SLICES
print(len(slices_list),len(set(cannon_slices_list)))
# 2000 SLICES generated by data augmentation has been reduced to 1 canonical SLICES