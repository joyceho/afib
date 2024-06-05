"""
modified C2Hest

Li, Yan-Guang, et al. "Refining age stratum of the C2HEST score for 
predicting incident atrial fibrillation in a hospital-based Chinese 
population." European journal of internal medicine 90 (2021): 37-42.
"""
import numpy as np

from afib import BaseRisk

MC2HEST_PTS = [1, 1, 1, 1, 2, 2, 1]


def mc2hest(cad, copd, htn, age, shf, hyperthyroid):
    """
    Calculates the modified C2Hest Risk score.

    Params:
    cad (bool): presence of coronary artery disease
    copd (bool): presence of chronic obstructive pulmonary disease
    htn (bool): presence of hypertension
    age (float): age of the person in years
    shf (bool): presence of systolic heart failure
    hyperthyroid (bool): hyperthroidism disease

    Returns:
    int: the c2hest score.

    Raises:
    TypeError: if bools not t/f, if ints/floats not a number.
    
    """
    arr = np.array([cad,
                    copd,
                    htn,
                    age >= 65 and age < 75,
                    age >= 75, 
                    shf,
                    hyperthyroid], dtype=int)
    return arr.dot(MC2HEST_PTS)

class MC2hest(BaseRisk):
    '''
    Class wrapper for modified C2HEST score
    '''
    features = ["cad", "copd", "htn", "index_age", "shf", "hyperthyroid"]
    feat_key = features
    
    def score(self, row):
        return mc2hest(row["cad"],
                       row["copd"],
                       row["htn"],
                       row["index_age"],
                       row["shf"],
                       row["hyperthyroid"])/8
