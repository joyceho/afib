import numpy as np

from afib import BaseRisk

NPOAF_PTS = [2,3,1,3,3,1]

def npoaf(age, mvd, lad):
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