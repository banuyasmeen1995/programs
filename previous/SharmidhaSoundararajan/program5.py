# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 13:28:00 2021

@author: sharmidha soundararajan
"""
#Program5

def calculateLbs(kg):
    lbs = kg*2.20462
    return lbs
    
def calculateOunces(kg):
    ounce = kg*35.274
    return ounce

def main():
    print ("Weight(Kg)\t\tLbs\t\t\t\t\tOunces")
    print ("----------------------------------------------------")
    for i in range (0,101,5):
        lbs = calculateLbs(i)
        ounces = calculateOunces(i)
        print ("%d\t\t\t\t%f\t\t\t%f" % (i, lbs, ounces))
        
main()
