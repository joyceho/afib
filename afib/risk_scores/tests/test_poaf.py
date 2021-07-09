import numpy.testing as npt

from afib.risk_scores import poaf, PoafC

def test_poaf():
    tmp = poaf(59, False, 15, False, False, (30/100), False)
    npt.assert_equal(tmp, 0)
    tmp = poaf(60, False, 15, False, False, (30/100), False)
    npt.assert_equal(tmp, 1)
    tmp = poaf(70, False, 15, False, False, (30/100), False)
    npt.assert_equal(tmp, 2)
    tmp = poaf(80, False, 15, False, False, (30/100), False)
    npt.assert_equal(tmp, 3)
    tmp = poaf(80, True, 15, False, False, (30/100), False)
    npt.assert_equal(tmp, 4)
    tmp = poaf(80, True, 14, False, False, (30/100), False)
    npt.assert_equal(tmp, 5)
    tmp = poaf(80, True, 14, True, False, (30/100), False)
    npt.assert_equal(tmp, 6)
    tmp = poaf(80, True, 14, True, True, (30/100), False)
    npt.assert_equal(tmp, 7)
    tmp = poaf(80, True, 14, True, True, (29/100), False)
    npt.assert_equal(tmp, 8)
    tmp = poaf(80, True, 14, True, True, (29/100), True)
    npt.assert_equal(tmp, 9)
    
def test_PoafC():
    model = PoafC()
    tmp = model.score({"age": 59,
                        "copd": False,
                        "egfr": 15,
                        "emrgncy": False,
                        "pibp": False,
                        "lvef": (30/100),
                        "vs": False})
    npt.assert_almost_equal(tmp, 0, decimal=3)
    tmp = model.score({"age": 60,
                        "copd": False,
                        "egfr": 15,
                        "emrgncy": False,
                        "pibp": False,
                        "lvef": (30/100),
                        "vs": False})
    npt.assert_almost_equal(tmp, 1, decimal=3)
    tmp = model.score({"age": 70,
                        "copd": False,
                        "egfr": 15,
                        "emrgncy": False,
                        "pibp": False,
                        "lvef": (30/100),
                        "vs": False})
    npt.assert_almost_equal(tmp, 2, decimal=3)
    tmp = model.score({"age": 80,
                        "copd": False,
                        "egfr": 15,
                        "emrgncy": False,
                        "pibp": False,
                        "lvef": (30/100),
                        "vs": False})
    npt.assert_almost_equal(tmp, 3, decimal=3)
    tmp = model.score({"age": 80,
                        "copd": True,
                        "egfr": 15,
                        "emrgncy": False,
                        "pibp": False,
                        "lvef": (30/100),
                        "vs": False})
    npt.assert_almost_equal(tmp, 4, decimal=3)
    tmp = model.score({"age": 80,
                        "copd": True,
                        "egfr": 14,
                        "emrgncy": False,
                        "pibp": False,
                        "lvef": (30/100),
                        "vs": False})
    npt.assert_almost_equal(tmp, 5, decimal=3)
    tmp = model.score({"age": 80,
                        "copd": True,
                        "egfr": 14,
                        "emrgncy": True,
                        "pibp": False,
                        "lvef": (30/100),
                        "vs": False})
    npt.assert_almost_equal(tmp, 6, decimal=3)
    tmp = model.score({"age": 80,
                        "copd": True,
                        "egfr": 14,
                        "emrgncy": True,
                        "pibp": True,
                        "lvef": (30/100),
                        "vs": False})
    npt.assert_almost_equal(tmp, 7, decimal=3)
    tmp = model.score({"age": 80,
                        "copd": True,
                        "egfr": 14,
                        "emrgncy": True,
                        "pibp": True,
                        "lvef": (29/100),
                        "vs": False})
    npt.assert_almost_equal(tmp, 8, decimal=3)
    tmp = model.score({"age": 80,
                        "copd": True,
                        "egfr": 14,
                        "emrgncy": True,
                        "pibp": True,
                        "lvef": (29/100),
                        "vs": True})
    npt.assert_almost_equal(tmp, 9, decimal=3)

test_PoafC()