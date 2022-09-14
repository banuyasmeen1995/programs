# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 13:57:02 2021

@author: sharmidha soundararajan
"""
import random
import string

def get_random_string():
    # choose from all lowercase letter
    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase
    character = lower_letters + upper_letters + "0123456789" + "!@#$%^&*"
    result_str = ''.join(random.choice(character) for i in range(10))
    return result_str

def generate_password():
    outfileName = "passwords.txt"
    outfile = open(outfileName,"w")
    for i in range(0,101):
        outfile.write(get_random_string())
        outfile. write("\n")
    outfile.close()
    
result_str = get_random_string() 
print("Random password is: ",result_str)
generate_password()


