import numpy as np
import pytest
from maxima import find_maxima

test_cases = [
( [0, 1, 2, 1, 2, 1, 0], [2,4] ),
( [-i**2 for i in range(-3, 4)] , [3] ),
( [np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)] , [16, 78] ),
( [4, 2, 1, 3, 1, 2], [0, 3, 5] ),
( [4, 2, 1, 3, 1, 5], [0, 3, 5] ) ,
( [4, 2, 1, 3, 1], [0, 3] )
]

@pytest.mark.parametrize('inp, exp', test_cases)
def test_maxima(inp, exp):
    out = find_maxima(inp)
    assert out == exp


def test_1():
    x = [0, 1, 2, 1, 2, 1, 0]
    y = [2,4]
    assert np.all(find_maxima(x) == y)


def test_2():
    x = [-i**2 for i in range(-3, 4)]
    y = [3]
    assert np.all(find_maxima(x) == y)     
