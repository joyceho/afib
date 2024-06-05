"""
HAVOC

Kwong, Calvin, et al. "A clinical score for predicting atrial fibrillation
 in patients with cryptogenic stroke or transient ischemic attack." 
Cardiology 138.3 (2017): 133-140.
"""
import numpy as np

from afib import BaseRisk

HAVOC_PTS = [2, 2, 2, 1, 1, 4, 2]


def havoc(htn, age, valvular, pvd, obesity, chf, cad):
    """
    Calculates the C2Hest Risk score.

    Params:
    htn (bool): presence of hypertension
    age (float): age of the person in years
    valve (bool): presence of vavlular heart disease)
    pvd (bool): presence of peripheral vascular disease
    obesity (bool): bmi > 30
    chf (bool): presence of congestive heart failure
    cad (bool): presence of coronary artery disease

    Returns:
    int: the HAVOC score.

    Raises:
    TypeError: if bools not t/f, if ints/floats not a number.
    
    """
    arr = np.array([htn,
                    age >= 75,
                    valvular,
                    pvd,
                    obesity,
                    chf,
                    cad], dtype=int)
    return arr.dot(HAVOC_PTS)

class Havoc(BaseRisk):
    '''
    Class wrapper for HAVOC score
    '''
    features = ["htn", "index_age", "valvular", "pvd", "obesity", "chf", "cad"]
    feat_key = features
    
    def score(self, row):
        return havoc(row["htn"],
                     row["index_age"],
                     row["valvular"],
                     row["pvd"],
                     row["obesity"],
                     row["chf"],
                     row["cad"])/14
