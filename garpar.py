#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:09:17 2021

@author: nadia
"""


import numpy as np
import pandas as pd


def ngenerator(tm1, random):
    i = random.normal(loc=tm1, scale=0.01)
    return tm1 + i


def sim(tn, an, seed, sol):
    random = np.random(seed)
    rows = []
    for t in range(tn):
        row= {}
        for a in range(an):
            name = f"Stock{a}"
            v = 0
            if t != 0:
                tm1= rows[t-1][name]
                v = sol(tm1, random)
                row[name] = v
        rows.append(row)
    return pd.DataFrame(rows)


#sim(100, 23, 42, ngenerator)