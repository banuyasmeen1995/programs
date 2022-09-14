# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 12:56:56 2021

@author: sharmidha soundararajan
"""

def main():
    print("This program will calculate average word length!")
    infile = open("word.txt","r")
    for line in infile:
        words = line.split()
        wordCount = len(words)
    ch = 0
    for word in words:
        ch+= len(word)
    avg = ch / wordCount
    print("Average word length is:", avg)
    infile.close()
main()