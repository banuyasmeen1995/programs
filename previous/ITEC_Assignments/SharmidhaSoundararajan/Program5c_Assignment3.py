# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 17:39:41 2021

@author: sharmidha soundararajan
"""


ASCII_SIZE = 256
 
def getMaxOccuringChar(str):
    encryption = ""

    count = [0] * ASCII_SIZE
 
    max = -1
    c = ''

    for i in str:
        count[ord(i)]+=1;
 
    for i in str:
        if max < count[ord(i)]:
            max = count[ord(i)]
            c = i
 
    key = ord(c)-ord("E")
    for letter in str:
        letter_unicode = ord(letter)
        letter_index = ord(letter)-ord("A")
        new_index = (letter_index-key)%26
        new_unicode = new_index+ord("A")
        new_char = chr(new_unicode)
        encryption = encryption+new_char
    print("key is: ",key)
    print("Result is ",encryption)
    
    return c
 
str = "SIOBUPYWLUWEYXNBYWIXY"
getMaxOccuringChar(str)


