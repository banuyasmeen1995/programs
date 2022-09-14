# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 12:19:01 2021

@author: sharmidha soundararajan
"""

import numpy as np 
import matplotlib.pyplot as plt

g=9.8
y = np.arange(10,201)
root = np.sqrt(y/g)
t = 2*np.pi*root
plt.plot(y,t)
plt.xlabel("length of the pendulum string (cm) ")
plt.ylabel("pendulum period")