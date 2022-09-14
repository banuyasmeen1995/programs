# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 12:46:29 2021

@author: sharmidha soundararajan
"""
#Program6

sum = 1
total_no_of_grains=0
for i in range(1,64):
    sum+=sum
    total_no_of_grains+=sum
print("Total number of grains is: ",total_no_of_grains+1) 

  

