# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 17:11:07 2021

@author: sharm
"""

import numpy as np
import random

np.random.seed(10)

def generate_random():
        #generate random numbers for a pair of dice and add them
        dice1 = np.random.randint(1,6) 
        dice2 = np.random.randint(1,6)
        dice = dice1+dice2
        return dice

def main():
    lose = 0
    win=0
 
    for i in range(0,10000):
        roll = generate_random()
        if roll==2 or roll==3 or roll==12:
            lose+=1          
        elif roll==7 or roll==11:
            win+=1
        else:
            re_roll=0
            initial_roll=roll
            #re-roll the dice
            while (re_roll!=initial_roll):
                re_roll = generate_random()
                #check if the dice value is equal to 7 
                if re_roll == 7:
                   lose+=1
                   break 

            if re_roll==initial_roll:
                win+=1

    probabiltity = win/10000
    print("Probabiltity of winning is: ",probabiltity)
main()
            
            