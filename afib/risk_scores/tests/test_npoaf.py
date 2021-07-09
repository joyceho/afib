import numpy.testing as npt

from afib.risk_scores import npoaf, NPoafC

def test_npoaf():
    tmp = npoaf(64, "None", False)
    npt.assert_equal(tmp, 0)
    tmp = npoaf(65, "None", False)
    npt.assert_equal(tmp, 2)
    tmp = npoaf(75, "None", False)
    npt.assert_equal(tmp, 3)
    tmp = npoaf(75, "Mild", False)
    npt.assert_equal(tmp, 4)
    tmp = npoaf(75, "Moderate", False)
    npt.assert_equal(tmp, 6)
    tmp = npoaf(75, "Severe", False)
    npt.assert_equal(tmp, 6)
    tmp = npoaf(75, "Severe", True)
    npt.assert_equal(tmp, 7)

def test_NPoafC():
    model = NPoafC()
    tmp = model.score({"age": 64,
                        "mvd": "None",
                        "lad": False})
    npt.assert_almost_equal(tmp, 0, decimal=3)
    tmp = model.score({"age": 65,
                        "mvd": "None",
                        "lad": False})
    npt.assert_almost_equal(tmp, 2, decimal=3)
    tmp = model.score({"age": 75,
                        "mvd": "None",
                        "lad": False})
    npt.assert_almost_equal(tmp, 3, decimal=3)
    tmp = model.score({"age": 75,
                        "mvd": "Mild",
                        "lad": False})
    npt.assert_almost_equal(tmp, 4, decimal=3)
    tmp = model.score({"age": 75,
                        "mvd": "Moderate",
                        "lad": False})
    npt.assert_almost_equal(tmp, 6, decimal=3)
    tmp = model.score({"age": 75,
                        "mvd": "Severe",
                        "lad": False})
    npt.assert_almost_equal(tmp, 6, decimal=3)
    tmp = model.score({"age": 75,
                        "mvd": "Severe",
                        "lad": True})
    npt.assert_almost_equal(tmp, 7, decimal=3)
