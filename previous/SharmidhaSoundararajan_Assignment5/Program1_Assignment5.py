# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 12:03:06 2021

@author: sharmidha soundararajan
"""

class TVShow:
    def __init__(self,title,genre,rating,noEpisodes,noSeasons):
        self.title=title
        self.genre=genre
        self.rating=rating
        self.noEpisodes=noEpisodes
        self.noSeasons=noSeasons

    def __str__(self):
        return self.title+","+self.genre


show=TVShow("Money Heist","Action",4.8,10,5)
print("Favourite TV show is:", show)
  
