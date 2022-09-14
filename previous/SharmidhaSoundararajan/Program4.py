# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 11:32:04 2021

@author: sharmidha soundararajan
"""

#Program4

def calculate(l,r):
    a = 3.14*(r**2)+2*r*l
    return a

def main():
    length = eval(input("Enter the length of rectangle: "))
    radius = eval(input("Enter the radius of semicircle half : "))
    area = calculate(length,radius)
    print("Area of the stadium is: ",area)
    
main()
