#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:09:17 2021

@author: nadia
"""


import numpy as np
import pandas as pd

_ENT = -1 / np.log2(2)


def risso_candidate_entropy(windows_size=4):
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
    return modificated_entropy


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
