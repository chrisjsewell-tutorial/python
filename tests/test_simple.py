from cjs_tutorial.lib import psi_squared


def test_psi_squared():
    """Test psi_squared()"""
    assert [round(x, 2) for x in psi_squared(0, [1, 2])] == [0.21, 0.01]
