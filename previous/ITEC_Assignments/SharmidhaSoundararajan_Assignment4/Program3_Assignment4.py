# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 14:13:29 2021

@author: sharm
"""

import numpy as np

np.random.seed(10)

shared_birthday = 0
probabilities = []
size = 30
for i in range(0,100):

    # generate random dates to 30 memebers
    dates = np.random.choice(range(1,366), size=30)

    # check if there are duplicates
    if len(np.unique(dates)) != len(dates):
        shared_birthday+=1 

    probability = shared_birthday/100
    probabilities.append(probability)

print("Probability at least two students share a birthday is:" , probability)

