import numpy.testing as npt

from afib.stroke import chad, Chads2


def test_chad():
    tmp = chad(False, False, 45, False, False)
    npt.assert_equal(tmp, 0)
    tmp = chad(True, False, 45, False, False)
    npt.assert_equal(tmp, 1)
    tmp = chad(True, True, 45, False, False)
    npt.assert_equal(tmp, 2)
    tmp = chad(True, True, 50, True, False)
    npt.assert_equal(tmp, 3)
    tmp = chad(True, True, 76, True, False)
    npt.assert_equal(tmp, 4)
    tmp = chad(True, True, 76, True, True)
    npt.assert_equal(tmp, 6)


def test_chads2():
    model = Chads2()
    tmp = model.score({"index_age": 45,
                       "chf": False,
                       "htn": False,
                       "dm": False,
                       "stroke": False})
    npt.assert_almost_equal(tmp, 0, decimal=3)
    tmp = model.score({"index_age": 45,
                       "chf": True,
                       "htn": False,
                       "dm": False,
                       "stroke": False})
    npt.assert_almost_equal(tmp, 1, decimal=3)
    tmp = model.score({"index_age": 45,
                       "chf": True,
                       "htn": True,
                       "dm": False,
                       "stroke": False})
    npt.assert_almost_equal(tmp, 2, decimal=3)
    tmp = model.score({"index_age": 50,
                       "chf": True,
                       "htn": True,
                       "dm": True,
                       "stroke": False})
    npt.assert_almost_equal(tmp, 3, decimal=3)
    tmp = model.score({"index_age": 76,
                       "chf": True,
                       "htn": True,
                       "dm": True,
                       "stroke": False})
    npt.assert_almost_equal(tmp, 4, decimal=3)
    tmp = model.score({"index_age": 76,
                       "chf": True,
                       "htn": True,
                       "dm": True,
                       "stroke": True})
    npt.assert_almost_equal(tmp, 6, decimal=3)
