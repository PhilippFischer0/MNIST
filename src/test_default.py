import src
import numpy as np


def test_foo():
    assert True

def test_forward():
    x = np.random.uniform(0, 10, 20)

    FF = src.FeedForward(20, 1024, 5)
    out = FF(x)

    assert len(out) == 5
    assert sum(np.round(out, 6)) == 1