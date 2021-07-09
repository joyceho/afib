import numpy.testing as npt

from afib.risk_scores import care, CareC

def test_care():
    tmp = care(False, False, False, False, False)
    npt.assert_equal(tmp, 0)
    tmp = care(True, True, False, False, False)
    npt.assert_equal(tmp, 1)
    tmp = care(False, True, False, False, False)
    npt.assert_equal(tmp, 2)
    tmp = care(False, False, True, False, False)
    npt.assert_equal(tmp, 3)
    tmp = care(False, False, False, True, False)
    npt.assert_equal(tmp, 4)
    tmp = care(False, False, False, False, True)
    npt.assert_equal(tmp, 5)

def test_CareC():
    model = CareC()
    tmp = model.score({"cd": False,
                        "cdmp": False,
                        "_or": False,
                        "_and": False,
                        "lh": False})
    npt.assert_almost_equal(tmp, 0, decimal=3)
    tmp = model.score({"cd": True,
                        "cdmp": False,
                        "_or": False,
                        "_and": False,
                        "lh": False})
    npt.assert_almost_equal(tmp, 1, decimal=3)
    tmp = model.score({"cd": False,
                        "cdmp": True,
                        "_or": False,
                        "_and": False,
                        "lh": False})
    npt.assert_almost_equal(tmp, 2, decimal=3)
    tmp = model.score({"cd": False,
                        "cdmp": False,
                        "_or": True,
                        "_and": False,
                        "lh": False})
    npt.assert_almost_equal(tmp, 3, decimal=3)
    tmp = model.score({"cd": False,
                        "cdmp": False,
                        "_or": False,
                        "_and": True,
                        "lh": False})
    npt.assert_almost_equal(tmp, 4, decimal=3)
    tmp = model.score({"cd": False,
                        "cdmp": False,
                        "_or": False,
                        "_and": False,
                        "lh": True})
    npt.assert_almost_equal(tmp, 5, decimal=3)

test_care()