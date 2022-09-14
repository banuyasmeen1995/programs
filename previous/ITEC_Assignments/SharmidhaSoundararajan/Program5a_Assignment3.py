# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 16:20:19 2021

@author: sharmidha soundararajan
"""
t = input("Enter a message: ")
key = 2
encryption = ""
text = t.replace(" ","")

for letter in text:
    letter_unicode = ord(letter)
    letter_index = ord(letter)-ord("A")
    new_index = (letter_index+key)%26
    new_unicode = new_index+ord("A")
    new_char = chr(new_unicode)
    encryption = encryption+new_char
    
print(encryption)

