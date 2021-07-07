import numpy as np

from afib import BaseRisk

POAF_PTS = [1,2,3,1,1,1,1,1,1]

def poaf(age, copd, egfr, emrgncy, pibp, lvef, vs):
    arr = np.array([60 <= age <= 69, 
                    70 <= age <= 79,
                    age >= 80,
                    copd, 
                    egfr < 15, 
                    emrgncy, 
                    pibp, 
                    lvef < (30/100), 
                    vs], dtype=int)
    return arr.dot(POAF_PTS)


class PoafC(BaseRisk):
    #array = ["age","copd","egfr","emrgncy","pibp","lvef","vs"]

    def score(self, row):
        return poaf(row["age"],
                    row["copd"],
                    row["egfr"],
                    row["emrgncy"],
                    row["pibp"],
                    row["lvef"],
                    row["vs"])