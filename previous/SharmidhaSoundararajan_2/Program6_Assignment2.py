# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 16:02:23 2021

@author: sharmidha soundararajan
"""
import graphics
from graphics import *
def main():
    win = GraphWin('polygon',600,600)
    p1 = Point(100,500)
    p2 = Point(250,300)
    p3 = Point(100,100)
    p4 = Point(400,100)
    p5 = Point(550,300)
    p6 = Point(400,500)
    polygon = Polygon(p1,p2,p3,p4,p5,p6)
    colour = input("Enter your favourite colour: ")
    polygon.setFill(colour)
    polygon.setOutline(colour)
    polygon.draw(win)
    input('Press ENTER to close the window')
    win.close()
    
main()