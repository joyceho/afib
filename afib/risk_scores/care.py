"""
Dupuis, J. Y., Wang, F., Nathan, H., Lam, M., 
Grimes, S., & Bourke, M. (2001). The cardiac 
anesthesia risk evaluation score: a clinically 
useful predictor of mortality and morbidity after 
cardiac surgery. The Journal of the American 
Society of Anesthesiologists, 94(2), 194-204.
"""
#Author: Eduardo Valverde

import numpy as np

from afib import BaseRisk

#CARE_PTS = [1,2,3,4,5]

def care(cd, cdmp, _or, _and, lh):
    """Calculates CARE score.

    Args:
        cd: t/f has stable cardiac disease, no other medical problems, undergoing noncomplex surgery.
        cdmp: t/f has stable cardiac disease, one or more controlled medical problems, undergoing noncomplex surgery.
        _or: t/f has had any uncontrolled medical problem OR undergoing complex surgery.
        _and: t/f has had any uncontrolled medical problem AND undergoing complex surgery.
        lh: t/f has chronic or advanced cardiac disease undergoing cardiac surgery as a last hope to save or improve life.
    Returns:
        the CARE score.
    Raises:
        TypeError: if bools not t/f.

    """
    score = 0
    if (cd):
        score = 1
    elif(cdmp):
        score = 2
    elif(_or):
        score = 3
    elif(_and):
        score = 4
    elif(lh):
        score = 5
    return score

class CareC(BaseRisk):
    #array = ["cd","cdmp","_or","_and","lh"]

    def score(self, row):
        return care(row["cd"],
                    row["cdmp"],
                    row["_or"],
                    row["_and"],
                    row["lh"])