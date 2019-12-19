import pytest
from .operations import Operations


def test_add():
    assert Operations.martin_chaia_function([1, 2, 6], Operations.add) == 9
    assert Operations.martin_chaia_function([i for i in range(10)], Operations.add) == 45
    assert Operations.martin_chaia_function([i % 10 for i in range(10000)], Operations.add) == 45000


def test_cube():
    assert Operations.martin_chaia_function([1, 2, 6], Operations.cube) == 225
    assert Operations.martin_chaia_function([i for i in range(10)], Operations.cube) == 2025
    assert Operations.martin_chaia_function([i % 10 for i in range(10000)], Operations.cube) == 2025000


def test_inverse_multiplicative():
    assert round(Operations.martin_chaia_function([1, 2, 6], Operations.inverse_multiplicative), 2) == 1.67
    assert round(Operations.martin_chaia_function([i+1 for i in range(10)], Operations.inverse_multiplicative), 2) == 2.93

    with pytest.raises(AssertionError):
        assert Operations.martin_chaia_function([i for i in range(10)], Operations.inverse_multiplicative)
