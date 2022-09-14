# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 22:09:56 2021

@author: sharmidha soundararajan
"""

from graphics import *
def main():
    win = GraphWin('Pentagon',300,300)
    print("Click five times in the window to draw the pentagon")
    point1 = win.getMouse()
    point2 = win.getMouse()
    point3 = win.getMouse()
    point4 = win.getMouse()
    point5 = win.getMouse()
    pentagon = Polygon(point1,point2,point3,point4,point5)
    pentagon.setFill("green")
    pentagon.setOutline("green")
    pentagon.draw(win)
    input('Press ENTER to close the window')
    win.close()
    
main()