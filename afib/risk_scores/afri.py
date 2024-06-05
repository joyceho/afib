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

AFRI_PTS = [1,1,1,1]

def afri_male(age, wt, height, pvd):
    """Calculates AFRI score for males.

    Args:
        age: age of person in years.
        wt: weight of person in kg.
        height: height of person in cm.
        pvd: t/f has peripheral vascular disease.
    Returns:
        the male-specific AFRI score.
    Raises:
        TypeError: if bools not t/f, if ints not a number.

    """
    arr = np.array([60 < age, 
                    76 < wt,
                    176 < height,
                    pvd], dtype=int)
    return arr.dot(AFRI_PTS)

def afri_female(age, wt, height, pvd):
    """Calculates AFRI score for females.

    Args:
        age: age of person in years.
        wt: weight of person in kg.
        height height of person in cm.
        pvd: t/f has peripheral vascular disease.
    Returns:
        the female-specific AFRI score.
    Raises:
        TypeError: if bools not t/f, if ints not a number.

    """
    arr = np.array([66 < age, 
                    64 < wt,
                    168 < height,
                    pvd], dtype=int)
    return arr.dot(AFRI_PTS)


def afri(female, age, wt, height, pvd):
    if female:
        return afri_female(age, wt, height, pvd)
    else:
        return afri_male(age, wt, height, pvd)

    
class Afri(BaseRisk):
    features = ["female", "index_age", "weight_kg", 
                "height_m", "pvd"]
    feat_key = features
    
    def score(self, row):
        return afri(row["female"],
                    row["index_age"],
                    row["weight_kg"],
                    row["height_m"]*100,
                    row["pvd"])/4

