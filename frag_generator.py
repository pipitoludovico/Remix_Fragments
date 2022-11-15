from rdkit import Chem
from rdkit.Chem import BRICS


# CN(CC1=C(C(=CC(=C1)Br)Br)N)C2CCCCC2.Cl

class FragGenerator:
    def __init__(self):
        self.fragments = []
        # self.scaffold = input('Insert SMILES of the scaffold: ')
        self.scaffold = Chem.MolFromSmiles('CN(CC1=C(C(=CC(=C1)Br)Br)N)C2CCCCC2.Cl')
        self.frags = BRICS.BRICSDecompose(self.scaffold)

    def getFragments(self):
        return self.fragments

    def showFrags(self):
        for frag in self.frags:
            self.fragments.append(frag)
            print(frag)
