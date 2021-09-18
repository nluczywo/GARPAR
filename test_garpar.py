import numpy as np
import pytest

import garpar as gp


@pytest.mark.parametrize(
    "windows_size, h",
    [
        (1, [0.0, 0.0]),
        (2, [0.0, 1.0, 0.0]),
        (3, [0.0, 0.91830, 0.91830, 0.0]),
        (4, [0.0, 0.81127, 1.0, 0.81127, 0.0]),
        (5, [0.0, 0.72193, 0.97095, 0.97095, 0.72193, 0.0]),
        (6, [0.0, 0.65002, 0.91830, 1.0, 0.91830, 0.65002, 0.0]),
        (7, [0.0, 0.59167, 0.86312, 0.98522, 0.98522, 0.86312, 0.59167, 0.0]),
    ],
)
def test_risso_candidate_entropy(windows_size, h):
    result = gp.risso_candidate_entropy(windows_size)
    assert np.allclose(result, h, atol=1e-05)


@pytest.mark.parametrize("windows_size", [0, -1])
def test_risso_candidate_entropy_le0(windows_size):
    with pytest.raises(ValueError):
        gp.risso_candidate_entropy(windows_size)


def test_nearest():
    assert gp.nearest([0.1, -0.98], 0) == 0.1
    assert gp.nearest([0.1, -0.98], -0.99) == -0.98
