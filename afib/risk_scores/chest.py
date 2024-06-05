"""
C2Hest

Li, Yan-Guang, et al. "A simple clinical risk score (C2HEST) for predicting 
incident atrial fibrillation in Asian subjects: derivation in 471,446 
Chinese subjects, with internal validation and external application in 
451,199 Korean subjects." Chest 155.3 (2019): 510-518.
"""
import numpy as np

from afib import BaseRisk

C2HEST_PTS = [1, 1, 1, 2, 2, 1]


def c2hest(cad, copd, htn, age, shf, hyperthyroid):
    """
    Calculates the C2Hest Risk score.

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
                    age >= 75, 
                    shf,
                    hyperthyroid], dtype=int)
    return arr.dot(C2HEST_PTS)

class C2hest(BaseRisk):
    '''
    Class wrapper for C2HEST score
    '''
    features = ["cad", "copd", "htn", "index_age", "shf", "hyperthyroid"]
    feat_key = features
    
    def score(self, row):
        return c2hest(row["cad"],
                      row["copd"],
                      row["htn"],
                      row["index_age"],
                      row["shf"],
                      row["hyperthyroid"])/8
