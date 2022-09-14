# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 12:36:34 2021

@author: sharmidha soundararajan
"""

infileName = "countryLists.txt"
infile = open(infileName,"r")
outfileName = "helloworld.txt"
outfile = open(outfileName,"w")
for line in infile:
    greeting = ("Hello "+line)
    outfile.write(greeting)
infile.close()
outfile.close() 

print("Result saved in output file")

