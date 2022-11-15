from brics import *
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors, PandasTools
from rdkit.ML.Descriptors import MoleculeDescriptors


class DfGenerator:
    def __init__(self, frags):
        self.df = pd.DataFrame(frags, columns=['SMILES'])
        self.mols = []
        self.Mol_descriptors = []
        self.mols = [Chem.MolFromSmiles(i) for i in self.df['SMILES']]

        self.calc = MoleculeDescriptors.MolecularDescriptorCalculator([x[0] for x in Descriptors._descList])
        self.desc_names = self.calc.GetDescriptorNames()
        for self.mol in self.mols:
            self.descriptors = self.calc.CalcDescriptors(self.mol)
            self.Mol_descriptors.append(self.descriptors)

    def printDF(self):
        return self.df

    def getDescr(self):
        return self.Mol_descriptors, self.desc_names

    def output(self):
        brics_generator = Brics()
        brics_generator.brics()
        brics_generator.buildBrics()
        frags = brics_generator.newBrics()

        self.dfgenerator = DfGenerator(frags)
        Mol_desc, desc_name = self.getDescr()
        df_full_descr = pd.DataFrame(Mol_desc, columns=desc_name)
        clean_df = df_full_descr[
            ['ExactMolWt', 'TPSA', 'NumHAcceptors', 'NumHDonors', 'NumAromaticRings',
             'NumRotatableBonds',
             'MolLogP']]
        ddf = self.printDF().join(clean_df, how='left')
        PandasTools.AddMoleculeColumnToFrame(ddf, smilesCol='SMILES')
        ddf.dropna(axis=1, how="any", inplace=True)
        PandasTools.SaveXlsxFromFrame(ddf, 'output.xlsx', molCol='ROMol')
        print(ddf)