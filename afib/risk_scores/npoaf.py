"""
Tran, D. T., Perry, J. J., Dupuis, J. Y., Elmestekawy, 
E., & Wells, G. A. (2015). Predicting new-onset 
postoperative atrial fibrillation in cardiac surgery 
patients. Journal of cardiothoracic and vascular 
anesthesia, 29(5), 1117-1126.
"""
#Author: Eduardo Valverde

import numpy as np

from afib import BaseRisk

NPOAF_PTS = [2,3,1,3,3,1]

def npoaf(age, mvd, lad):
    """Calculates alternative POAF score (New-onset POAF score).

    Args:
        age: age of the person in years.
        mvd: has mitral valve disease, takes inputs 'None', 'Mild', 'Moderate' or 'Severe' (first letter capitalized).
        lad: t/f has left atrial dilatation. 
    Returns:
        the new-onset POAF score.
    Raises:
        TypeError: if inputs are incorrect type.

    """
    arr = np.array([65 <= age <= 74,
                    75 <= age,
                    int(float(mvd == "Mild")),
                    int(float(mvd == "Moderate")),
                    int(float(mvd == "Severe")),
                    lad], dtype=int)
    return arr.dot(NPOAF_PTS)

class NPoafC(BaseRisk):

    def score(self, row):
        return npoaf(row["age"],
                    row["mvd"],
                    row["lad"])