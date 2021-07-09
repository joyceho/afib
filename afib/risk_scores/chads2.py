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

# points for each variable
CHADS2_PTS = [1, 1, 2, 1, 2, 1, 1, 1]


def chad(chf, htn, age, dm, stroke, vd, fem):
    """Calculates CHA₂DS₂-VASc score.

    Args:
        chf: t/f has had congestive heart failure.
        htn: t/f has had hypertension.
        age: age of person in years. 
        dm: t/f has had diabetes mellitus.
        stroke: t/f has stroke history.
        vd: t/f has had vascular disease.
        fem: t/f is female.
    Returns:
        the CHA₂DS₂-VASc score.
    Raises:
        TypeError: if bools not t/f, if ints not a number.

    """
    feat = np.array([chf,
                     htn,
                     age >= 75,
                     dm, 
                     stroke,
                     vd,
                     65 <= age <= 74,
                     fem], dtype=int)
    return feat.dot(CHADS2_PTS)


class Chads2(BaseRisk):
    #features = ["chf","htn","index_age","dm","stroke","vd","fem"]

    def score(self, row):
        return chad(row["chf"],
                    row["htn"],
                    row["index_age"],
                    row["dm"],
                    row["stroke"],
                    row["vd"],
                    row["fem"])
