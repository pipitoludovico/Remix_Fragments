from frag_generator import *
import random


class Brics:
    def __init__(self):
        self.new_mols = []
        self.allfrags = set()
        self.molecule_generator = None

    def brics(self):
        supply = Chem.SDMolSupplier('test.sdf')
        for m in supply:
            if m is None:
                continue
            frags = BRICS.BRICSDecompose(m)
            self.allfrags.update(frags)

    def buildBrics(self):
        random.seed(0)
        fragments = [Chem.MolFromSmiles(x) for x in sorted(self.allfrags)]
        self.molecule_generator = BRICS.BRICSBuild(fragments)
        return self.molecule_generator

    def newBrics(self):
        prods = [next(self.molecule_generator) for _ in range(len(self.allfrags))]
        for prod in prods:
            prod.UpdatePropertyCache(strict=False)
            new_smile = Chem.MolToSmiles(prod)
            self.new_mols.append(new_smile)
        return self.new_mols
