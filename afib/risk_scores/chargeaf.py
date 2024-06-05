"""
Charge-AF

Alonso, Alvaro, et al. "Simple risk model predicts incidence of atrial fibrillation 
in a racially and geographically diverse population: the CHARGE‐AF consortium." 
Journal of the American Heart Association 2.2 (2013): e000102.
"""
import numpy as np

from afib import BaseRisk

CHARGEAF_PTS = [0.508, 0.465, 0.248, 0.115, 0.197, -0.101, 0.359, 0.349, 0.237, 0.701, 0.496]


def charge_af(age, white, height, weight, sbp, dbp, smoke, htn_treat, dm, chf, mi):
    """
    Calculates the Charge-AF risk score

    Args:
        age: age in years
        white: t/f if White ethnicity
        height: height in cm
        weight: weight in kg
    Returns:
        the CHARGE-AF score.
    Raises:
        TypeError: if bools not t/f, if ints/floats not a number.

    """
    arr = np.array([age / 5,
                    white,
                    height/10,
                    weight/15,
                    sbp/20,
                    dbp/10,
                    smoke,
                    htn_treat,
                    dm,
                    chf,
                    mi])
    bx = arr.dot(CHARGEAF_PTS)
    return 1 - 0.9718412736**np.exp(bx - 12.5815600)

class ChargeAF(BaseRisk):
    '''

    '''
    features = ["index_age", "Cauc", "height_m", "weight_kg", "sbp", "dbp",
                "cur_smoke", "htn_treat", "dm", "chf", "mi"]
    feat_key = features
    
    def score(self, row):
        return charge_af(row["index_age"],
                         row["Cauc"],
                         row["height_m"]*100,
                         row["weight_kg"],
                         row["sbp"],
                         row["dbp"],
                         row["cur_smoke"],
                         row["htn_treat"],
                         row["dm"],
                         row["chf"],
                         row["mi"])
