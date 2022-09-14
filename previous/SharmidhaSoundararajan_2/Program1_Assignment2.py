# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 22:09:56 2021

@author: sharmidha soundararajan
"""

import math
def main():
    standard_potential = 1.25
    temperature = 273
    ion_charge = 2
    q = 0.077
    r = 8.3145
    f = 96485.33

    reduction_potential = standard_potential - ((r*temperature)/(ion_charge*f)) * math.log(q)
    print("Reduction potential is",round(reduction_potential,2))
main()
