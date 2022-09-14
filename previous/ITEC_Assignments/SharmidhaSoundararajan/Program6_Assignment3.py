# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 18:54:24 2021

@author: sharmidha soundararajan
"""
from operator import itemgetter

def main():
    count = 0
    max = -1
    c = ''
    freq = {}
    end_letter = {}
    infile = open("caesers.txt","r")
    for line in infile:
        for character in line:
            if character in freq:
               freq[character] +=1
            else:
                freq[character] =1
    
    frequencies= dict(sorted(freq.items(), key=lambda item: item[1])) 
    print("Frequency of each letters is ")
    print(frequencies)
    
    infiles = open("caesers.txt","r")
    for line in infiles:
        for i in line.split():
            if i[-1] in end_letter:
                end_letter[i[-1]] += 1
            else:
                end_letter[i[-1]] = 1
                
    endletter_freq= dict(sorted(end_letter.items(), key=lambda item: item[1])) 
    print("End frequencies is :")
    print(endletter_freq)
    
main()

