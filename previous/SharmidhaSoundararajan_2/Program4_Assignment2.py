# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 16:59:51 2021

@author: sharmidha soundararajan
"""
from graphics import *


def stripe(window,stripe,color):
    stripe.setFill(color)
    stripe.setOutline(color)
    stripe.draw(window)

def iceland_flag():
    flag_length = 600
    flag_height = 18 / 25 * flag_length
    win = GraphWin('Icelandflag',flag_length,flag_height)

    #RGB values of blue,red and white
    blue = color_rgb(2,85,156)
    red = color_rgb(220, 30, 53)
    white = color_rgb(255, 255, 255)
    
    stripe_colors = [blue,red,white]

    #set background colour with given rgb values for white
    win.setBackground(stripe_colors[2])

    # Blue rectangles
    blue_topleft = Rectangle(Point(0,0),Point(150,160))
    stripe(win,blue_topleft,stripe_colors[0])

    blue_bottomleft = Rectangle(Point(0,flag_height),Point(150,270))
    stripe(win,blue_bottomleft,stripe_colors[0])

    blue_topright = Rectangle(Point(flag_length,0),Point(260,160))
    stripe(win,blue_topright,stripe_colors[0])

    blue_bottomright = Rectangle(Point(flag_length,flag_height),Point(260,270))
    stripe(win,blue_bottomright,stripe_colors[0])

    #red stripe

    red_horizontal = Rectangle(Point(0,240),Point(flag_length,190))
    stripe(win,red_horizontal,stripe_colors[1])

    red_vertical = Rectangle(Point(230,0),Point(180,flag_length))
    stripe(win,red_vertical,stripe_colors[1])
    
    input('Press ENTER to close the window')
    win.close()
    
iceland_flag()