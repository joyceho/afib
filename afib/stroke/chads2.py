"""
"""
import numpy as np

from afib import BaseRisk

# points for each variable
CHADS2_PTS = [1, 1, 1, 1, 2]


def chad(chf, htn, age, dm, stroke):
    feat = np.array([chf,
                     htn,
                     age >= 75,
                     dm, 
                     stroke], dtype=int)
    return feat.dot(CHADS2_PTS)


class Chads2(BaseRisk):
    features = ["chf",
                "htn",
                "index_age",
                "dm",
                "stroke"]

    def score(self, row):
        return chad(row["chf"],
                    row["htn"],
                    row["index_age"],
                    row["dm"],
                    row["stroke"])
