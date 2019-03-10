
"""

基因类

"""

import  numpy as np
import pandas as pd


class Gene:

    def __init__(self):
        """Creates a Dna object.

        Keyword Arguments:
        bits -- String representation of bits.
        weights -- Integer list of weights
        values -- Integer list of values
        bag -- Bag object
        """

        self.dna= np.random.randint(0, 4, size=7)

    def set(self,dna):
        """Creates a Dna object.

        Keyword Arguments:
        bits -- String representation of bits.
        weights -- Integer list of weights
        values -- Integer list of values
        bag -- Bag object
        """

        self.dna = dna


    def __str__(self):
        return str(self.dna)

    def __repr__(self):
        return str(self)
