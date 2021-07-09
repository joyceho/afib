"""
Cameron, M. J., Tran, D. T., Abboud, J., Newton, 
E. K., Rashidian, H., & Dupuis, J. Y. (2018). 
Prospective external validation of three preoperative 
risk scores for prediction of new onset atrial 
fibrillation after cardiac surgery. Anesthesia & 
Analgesia, 126(1), 33-38.
"""
#Author: Eduardo Valverde

import numpy as np

from afib import BaseRisk

POAF_PTS = [1,2,3,1,1,1,1,1,1]

def poaf(age, copd, egfr, emrgncy, pibp, lvef, vs):
    """Calculates the POAF score.

    Args:
        age: age of the person in years.
        copd: t/f has chronic obstructive pulmonary disease.
        egfr: estimated glomerular filtration rate.
        emrgncy: t/f is emergency.
        pibp: t/f has had preoperative intra-aortic balloon pump.
        lvef: left ventricular ejection fraction (x/100).
        vs: t/f has had valve surgery.
    Returns:
        the POAF score.
    Raises:
        TypeError: if bools not t/f, if ints/floats not a number.

    """
    arr = np.array([60 <= age <= 69, 
                    70 <= age <= 79,
                    age >= 80,
                    copd, 
                    egfr < 15, 
                    emrgncy, 
                    pibp, 
                    lvef < (30/100), 
                    vs], dtype=int)
    return arr.dot(POAF_PTS)

class PoafC(BaseRisk):
    '''

    '''
    def score(self, row):
        return poaf(row["age"],
                    row["copd"],
                    row["egfr"],
                    row["emrgncy"],
                    row["pibp"],
                    row["lvef"],
                    row["vs"])
