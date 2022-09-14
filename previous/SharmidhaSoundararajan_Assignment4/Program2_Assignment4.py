# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 16:36:12 2021

@author: sharmidha soundararajan
"""

import random
from collections import Counter

def main():
    common = 0
    things = ["Common","Rare","Legendary"]
    chance = [94.3,5.1,0.6]
    randomlist = []
    rare = 0
    legendary = 0
    for i in range (1,500):
        results = random.choices(things,chance)
        for j in results:
            if(j == things[1]):
                rare+=1
            elif(j == things[2]):
                legendary+=1 

        # check if Rare card is not drawn after 9 attempts
        if i<9:
            if results==things[1]:
               break
        if (rare==0) and (i == 9):
            results = things[1]
            rare+=1

        #If a Legendary card is not drawn after 75 attempts, prob of drawing legendary, increases to 30%.
        if(i>=76) and (legendary==0):
                for j in results:
                    chance[2] = 30
                    chance[0] = 64.9 #decrease the probability of common to have total probabilty to 1

       #If a Legendary card is drawn after 75 attempts, put the probabilty back to normal
        elif(i>=76) and (legendary!=0):
                if(j == 'Legendary'):
                      chance[2] = 0.6
                      chance[0] = 94.3

    # check if Legendary card is not drawn after 89 attempts
        if (legendary==0) and (i == 89):
             results = 'Legendary'
             legendary+=1  

    print("Probability of drawing a rare card is: ", (rare/500)*100)
    print("Probability of drawing a Legendary card is: ", (legendary/500)*100)
main()     
        




        