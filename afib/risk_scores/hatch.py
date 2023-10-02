import numpy as np

from afib import BaseRisk

# points for each variable
HATCH_PTS = [1, 1, 2, 1, 2]


def hatch(htn, age, stroke, copd, chf):
    feat = np.array([htn,
                     age >= 75,
                     stroke,
                     copd,
                     chf], dtype=int)
    return feat.dot(HATCH_PTS)
    

class Hatch(BaseRisk):
    features = ["htn","index_age","stroke", "copd", "chf"]
    feat_key = features

    def score(self, row):
        return hatch(row["htn"],
                     row["index_age"],
                     row["stroke"],
                     row["copd"],
                     row["chf"])/7
    
