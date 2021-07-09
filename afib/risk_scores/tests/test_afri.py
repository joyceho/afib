import numpy.testing as npt

from afib.risk_scores import afriMale, afriFem, AfriMaleC, AfriFemC

def test_afriMale():
    tmp = afriMale(60, 76, 176, False)
    npt.assert_equal(tmp, 0)
    tmp = afriMale(61, 76, 176, False)
    npt.assert_equal(tmp, 1)
    tmp = afriMale(61, 77, 176, False)
    npt.assert_equal(tmp, 2)
    tmp = afriMale(61, 77, 177, False)
    npt.assert_equal(tmp, 3)
    tmp = afriMale(61, 77, 177, True)
    npt.assert_equal(tmp, 4)

def test_afriFem():
    tmp = afriFem(66, 64, 168, False)
    npt.assert_equal(tmp, 0)
    tmp = afriFem(67, 64, 168, False)
    npt.assert_equal(tmp, 1)
    tmp = afriFem(67, 65, 168, False)
    npt.assert_equal(tmp, 2)
    tmp = afriFem(67, 65, 169, False)
    npt.assert_equal(tmp, 3)
    tmp = afriFem(67, 65, 169, True)
    npt.assert_equal(tmp, 4)

def test_AfriMaleC():
    model = AfriMaleC()
    tmp = model.score({"age": 60,
                        "wt": 76,
                        "height": 176,
                        "pvd": False})
    npt.assert_almost_equal(tmp, 0, decimal=3)
    tmp = model.score({"age": 61,
                        "wt": 76,
                        "height": 176,
                        "pvd": False})
    npt.assert_almost_equal(tmp, 1, decimal=3)
    tmp = model.score({"age": 61,
                        "wt": 77,
                        "height": 176,
                        "pvd": False})
    npt.assert_almost_equal(tmp, 2, decimal=3)
    tmp = model.score({"age": 61,
                        "wt": 77,
                        "height": 177,
                        "pvd": False})
    npt.assert_almost_equal(tmp, 3, decimal=3)
    tmp = model.score({"age": 61,
                        "wt": 77,
                        "height": 177,
                        "pvd": True})
    npt.assert_almost_equal(tmp, 4, decimal=3)

def test_AfriFemC():
    model = AfriFemC()
    tmp = model.score({"age": 66,
                        "wt": 64,
                        "height": 168,
                        "pvd": False})
    npt.assert_almost_equal(tmp, 0, decimal=3)
    tmp = model.score({"age": 67,
                        "wt": 64,
                        "height": 168,
                        "pvd": False})
    npt.assert_almost_equal(tmp, 1, decimal=3)
    tmp = model.score({"age": 67,
                        "wt": 65,
                        "height": 168,
                        "pvd": False})
    npt.assert_almost_equal(tmp, 2, decimal=3)
    tmp = model.score({"age": 67,
                        "wt": 65,
                        "height": 169,
                        "pvd": False})
    npt.assert_almost_equal(tmp, 3, decimal=3)
    tmp = model.score({"age": 67,
                        "wt": 65,
                        "height": 169,
                        "pvd": True})
    npt.assert_almost_equal(tmp, 4, decimal=3)