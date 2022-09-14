# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 11:44:19 2021

@author: sharmidha soundararajan
"""

Birth_tree = {1:"Apple",2:"Willow",3:"Maple",4:"Elm",5:"Fig",6:"Cherry",7:"Walnut",8:"Oak",9:"Palm",10:"Olive",11:"Citrus",12:"Sprouts"}

def getBirthTree(month):
    month = int(month)
    index = month %12
    return Birth_tree[index]
month = input("Enter a month: ")
out = getBirthTree(month)
print("Birth tree is: ",out)