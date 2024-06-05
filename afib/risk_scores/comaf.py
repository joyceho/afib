"""
COM-AF

Burgos, Lucrecia M., et al. "New combined risk score to predict 
atrial fibrillation after cardiac surgery: COM-AF." Annals of 
cardiac anaesthesia 24.4 (2021): 458-463.

"""
import numpy as np

from afib import BaseRisk

COMAF_PTS = [3.14, 8.68, 3.36, 2.45, 2.33, 1.68, 1.72]


def com_af(age, female, hf, stroke, htn, dm):
    """
    Calculates the COM-AF Risk score.

    Params:
    age (float): age of the person in years.
    female (bool): is person a female?
    hf (bool): does the person have heart failure?
    stroke (bool): did the person have a stroke previously?
    htn (bool): does the person have hypertension?
    dm (bool): does the person have diabetes?
    
    Returns:
    the COM-AF score.
    
    Raises:
    TypeError: if bools not t/f, if ints/floats not a number.
    """
    arr = np.array([65 <= age < 75, 
                    age >= 75,
                    female,
                    hf, 
                    stroke, 
                    htn,
                    dm], dtype=int)
    return arr.dot(COMAF_PTS)


class ComAF(BaseRisk):
    '''
    Class that encapsulates the ComAF calculation.
    '''
    features = ["htn","index_age","stroke", "dm", "chf", "female"]
    feat_key = features
    
    def score(self, row):
        return com_af(row["index_age"],
                      row["female"],
                      row["chf"],
                      row["stroke"],
                      row["htn"],
                      row["dm"])/20.22
