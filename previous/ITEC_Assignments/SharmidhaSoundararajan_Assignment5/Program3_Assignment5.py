# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 22:43:11 2021

@author: sharmidha soundararajan
"""

def hexConvert(number):
    a=hex(number)
    value = a.replace("0x", "")
    return value

def info(f):
    """The hexConvert function converts an interger given by the user to hexadecimal value and the value is.=="""
    
    value = eval(input("Enter an integer: "))
    return f(value)

decorator=info(hexConvert)
print( info.__doc__,end=" ")
print(decorator)