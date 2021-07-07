"""
"""
import numpy as np

from afib import BaseRisk

# points for each variable
CHADS2_PTS = [1, 1, 2, 1, 2, 1, 1, 1]


def chad(chf, htn, age, dm, stroke, vd, fem):
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
