# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 15:47:33 2021

@author: sharmidha soundararajan
"""

import numpy as np 
import matplotlib.pyplot as plt

price = np.arange(0,21)
demand = 20 - (2*price)
supply = -10 + (2*price)
plt.plot(price,demand)
plt.plot(price,supply)
plt.title("Supply and Demand")
plt.xlabel("Price")
plt.ylabel("Quantity")
plt.legend(["Demand","Supply"])
print("Equilibrium price is 7.5$")