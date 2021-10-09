import garpar as gp

import numpy as np

import pandas as pd

import pytest


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
    me, _ = gp.risso_candidate_entropy(windows_size)
    assert np.allclose(me, h, atol=1e-05)


@pytest.mark.parametrize("windows_size", [0, -1])
def test_risso_candidate_entropy_le0(windows_size):
    with pytest.raises(ValueError):
        gp.risso_candidate_entropy(windows_size)


def test_argnearest():
    assert gp.argnearest([0.1, -0.98], 0) == 0
    assert gp.argnearest([0.1, -0.98], -0.99) == 1
    assert gp.argnearest([0.1, -0.10], 0.1) == 0


@pytest.mark.parametrize(
    "windows_size, sequence",
    [
        (1, [True]),
        (2, [False, True]),
        (3, [False, True, False]),
        (4, [False, True, False, True]),
        (5, [True, False, True, False, True]),
        (6, [True, False, True, False, True, False]),
        (7, [True, False, True, False, True, False, True]),
    ],
)
def test_loss_sequence(windows_size, sequence):
    result = gp.loss_sequence(
        loss_probability=0.33, windows_size=windows_size, seed=10
    )
    assert np.all(result == sequence)


def test_make_stock_price():
    assert gp.make_stock_price(100, True) < 100
    assert gp.make_stock_price(100, False) > 100
    assert gp.make_stock_price(0, False) == 0
    assert gp.make_stock_price(0, True) == 0


def test_make_market():

    expected = pd.DataFrame(
        {
            "window": [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
            "day": [0, 1, 2, 3, 4, 0, 1, 2, 3, 4],
            "stock_0_price": [
                100.12784040316728,
                100.44408299551087,
                100.46088415301516,
                101.31392808058874,
                100.43453010572591,
                100.8032808898084,
                101.7621634906374,
                102.64061379194467,
                102.69053970293092,
                102.87540206647618,
            ],
            "stock_1_price": [
                99.63455593563592,
                99.22182332403993,
                98.79100232103205,
                96.6493547201616,
                97.05576973654621,
                96.21561325958368,
                95.39113204389244,
                94.74053925606773,
                95.48379342727118,
                96.02694769557638,
            ],
        }
    )
    result = gp.make_market(
        window_number=2, windows_size=5, stock_number=2, seed=42
    )
    pd.testing.assert_frame_equal(result, expected, atol=1e-10)
