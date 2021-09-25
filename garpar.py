#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:09:17 2021

@author: nadia
"""


import numpy as np

_ENT = -1 / np.log2(2)


def risso_candidate_entropy(windows_size):
    if windows_size <= 0:
        raise ValueError("'windows_size' must be > 0")

    probability_loss = np.linspace(0.0, 1.0, num=windows_size + 1)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(probability_loss.dtype).eps
    probability_loss[0] = epsilon
    probability_loss[-1] = 1 - epsilon

    # Calcula entropy
    first_part = probability_loss * np.log2(probability_loss)
    second_part = (1 - probability_loss) * np.log2(1 - probability_loss)

    modificated_entropy = _ENT * (first_part + second_part)
    return modificated_entropy, probability_loss


def argnearest(arr, v):
    diff = np.abs(np.subtract(arr, v))
    idx = np.argmin(diff)
    return idx


def loss_sequence(windows_size, probability_loss=0.5, seed=None):
    random = np.random.default_rng(seed=seed)
    probability_win = 1 - probability_loss
    sequence = random.choice(
        [True, False], size=windows_size, p=[probability_loss, probability_win]
    )
    if random.choice([True, False]):
        sequence = ~sequence
    return sequence


def make_stock_price(price, loss, seed=None):
    random = np.random.default_rng(seed=seed)
    sign = -1 if loss else 1
    day_return = sign * np.abs(random.normal(0, 1))
    new_price = price + day_return
    return new_price


# def ngenerator(tm1, random):
#    i = random.normal(loc=tm1, scale=0.01)
#    return tm1 + i


# def sim(tn, an, seed, sol):
#    random = np.random(seed)
#    rows = []
#    for t in range(tn):
#        row= {}
#        for a in range(an):
#            name = f"Stock{a}"
#            v = 0
#            if t != 0:
#                tm1= rows[t-1][name]
#                v = sol(tm1, random)
#                row[name] = v
#        rows.append(row)
#    return pd.DataFrame(rows)


# sim(100, 23, 42, ngenerator)
