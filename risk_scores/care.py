import numpy as np

from afib import BaseRisk

#CARE_PTS = [1,2,3,4,5]

def care(cd, cdmp, _or, _and, lh):
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