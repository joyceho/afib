import numpy as np

from afib import BaseRisk

AFRI_PTS = [1,1,1,1]

def afriMale(age, wt, height, pvd):
    arr = np.array([60 < age, 
                    76 < wt,
                    176 < height,
                    pvd], dtype=int)
    return arr.dot(AFRI_PTS)

def afriFem(age, wt, height, pvd):
    arr = np.array([66 < age, 
                    64 < wt,
                    168 < height,
                    pvd], dtype=int)
    return arr.dot(AFRI_PTS)

class AfriMaleC(BaseRisk):
    #array = ["age","wt","height","pvd"]

    def score(self, row):
        return afriMale(row["age"],
                    row["wt"],
                    row["height"],
                    row["pvd"])

class AfriFemC(BaseRisk):
    #array = ["age","wt","height","pvd"]

    def score(self, row):
        return afriFem(row["age"],
                    row["wt"],
                    row["height"],
                    row["pvd"])