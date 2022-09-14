# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 22:53:14 2021

@author: sharmidha soundararajan
"""

dict={}

letter = input("Enter a scrabble letter: ")
while letter!="": 
    
    dict[letter]= ord(letter)-96 
    letter = input("Enter a scrabble letter: ")
    
total_sum = sum(dict.values())

print("Total count is: ", total_sum)
