import numpy.testing as npt

from afib.risk_scores import chad, Chads2

def test_chad():
    tmp = chad(False, False, 45, False, False, False, False)
    npt.assert_equal(tmp, 0)
    tmp = chad(True, False, 45, False, False, False, False)
    npt.assert_equal(tmp, 1)
    tmp = chad(True, True, 45, False, False, False, False)
    npt.assert_equal(tmp, 2)
    tmp = chad(True, True, 65, False, False, False, False)
    npt.assert_equal(tmp, 3)
    tmp = chad(True, True, 75, False, False, False, False)
    npt.assert_equal(tmp, 4)
    tmp = chad(True, True, 75, True, False, False, False)
    npt.assert_equal(tmp, 5)
    tmp = chad(True, True, 75, True, True, False, False)
    npt.assert_equal(tmp, 7)
    tmp = chad(True, True, 75, True, True, True, False)
    npt.assert_equal(tmp, 8)
    tmp = chad(True, True, 75, True, True, True, True)
    npt.assert_equal(tmp, 9)


def test_chads2():
    model = Chads2()
    tmp = model.score({"index_age": 45,
                       "chf": False,
                       "htn": False,
                       "dm": False,
                       "stroke": False,
                       "vd": False,
                       "fem": False})
    npt.assert_almost_equal(tmp, 0, decimal=3)
    tmp = model.score({"index_age": 65,
                       "chf": False,
                       "htn": False,
                       "dm": False,
                       "stroke": False,
                       "vd": False,
                       "fem": False})
    npt.assert_almost_equal(tmp, 1, decimal=3)
    tmp = model.score({"index_age": 75,
                       "chf": False,
                       "htn": False,
                       "dm": False,
                       "stroke": False,
                       "vd": False,
                       "fem": False})
    npt.assert_almost_equal(tmp, 2, decimal=3)
    tmp = model.score({"index_age": 75,
                       "chf": True,
                       "htn": False,
                       "dm": False,
                       "stroke": False,
                       "vd": False,
                       "fem": False})
    npt.assert_almost_equal(tmp, 3, decimal=3)
    tmp = model.score({"index_age": 76,
                       "chf": True,
                       "htn": True,
                       "dm": False,
                       "stroke": False,
                       "vd": False,
                       "fem": False})
    npt.assert_almost_equal(tmp, 4, decimal=3)
    tmp = model.score({"index_age": 76,
                       "chf": True,
                       "htn": True,
                       "dm": True,
                       "stroke": False,
                       "vd": False,
                       "fem": False})
    npt.assert_almost_equal(tmp, 5, decimal=3)
    tmp = model.score({"index_age": 76,
                       "chf": True,
                       "htn": True,
                       "dm": True,
                       "stroke": True,
                       "vd": False,
                       "fem": False})
    npt.assert_almost_equal(tmp, 7, decimal=3)
    tmp = model.score({"index_age": 76,
                       "chf": True,
                       "htn": True,
                       "dm": True,
                       "stroke": True,
                       "vd": True,
                       "fem": False})
    npt.assert_almost_equal(tmp, 8, decimal=3)
    tmp = model.score({"index_age": 76,
                       "chf": True,
                       "htn": True,
                       "dm": True,
                       "stroke": True,
                       "vd": True,
                       "fem": True})
    npt.assert_almost_equal(tmp, 9, decimal=3)