"""

"""
import numpy as np

from afib import BaseRisk

# points for each variable
APPLE_PTS = [1, 1, 1, 1, 1]

# The APPLE score includes age≥65 years, persistent AF, impairedeGFR (<60 mL/min/1.73 m2), LA diameter≥43 mm, EF < 50%(1 point for each variable). Therefore, a maximum of five points couldbe achieved. The APPLE score can be used for the prediction ofelectro-anatomical substrate and recurrences after first and repeatedCA in AF patients.16,20

def apple(age, persist_af, egfr, la_diameter, ef):
    feat = np.array([age >= 65,
                     persist_af,
                     egfr < 60,
                     la_diameter, 
                     ef < 50], dtype=int)
    return feat.dot(APPLE_PTS)


class Apple(BaseRisk):
    features = ["chf",
                "htn",
                "age",
                "dm",
                "stroke"]

    def score(self, row):
        return apple(row["chf"],
                    row["htn"],
                    row["age"],
                    row["dm"],
                    row["stroke"])


    def get_json_feat(self, jsonEnc):
        return {}
