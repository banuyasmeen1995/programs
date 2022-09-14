# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 20:47:55 2021

@author: sharmidha soundararajan
"""

import random
class PlayingCard:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
  
    def getRank(self):
        return self.rank
  
    def getSuit(self):
        return self.suit
  
    def value(self):
        if self.rank>9:
            return 10
        else:
            return self.rank   
  
    def convertRank(self):
        if self.rank <12:
            hexRank ='{0:x}'.format(self.rank)
        else:
            hexRank = '{0:x}'.format(self.rank+1)
            return hexRank
  
    def convertSuit(self):
        suitDictHex = {"h":"b","d":"c","c":"d","s":"a"}
        return suitDictHex[self.suit]
  
    def __str__(self):
        hexValue = "1f0"+self.convertSuit()+self.convertRank()
        decValue = int(hexValue,16)
        return chr(decValue)


class Deck:
  
   def __init__(self):
       self.cardDeck = []
       for r in range(1,14): #ranks
           for s in 'c','d','h','s': #suits
               self.cardDeck.append(PlayingCard(r,s))
              
   def shuffle(self):
       random.shuffle(self.cardDeck)
      
   def dealCard(self):
       card = self.cardDeck.pop(0)
       return card
      
   def cardsLeft(self):
       return len(self.cardDeck)
      
   def printDeck(self):
        for card in self.cardDeck:
           print(card,end= " ")
          
   def sortbySuit(self):
       self.cardDeck.sort(key=PlayingCard.getSuit)
      
   def sortbyRank(self):
       self.cardDeck.sort(key=PlayingCard.getRank)
       
class Player :
  
   def __init__(self, name):
       self.name = name
       self.hand = []
      
   def drawCard(self, deck):
       self.hand.append(deck.dealCard())
      
   def playCard(self, card):
       for i in range(len(self.hand)):
              if self.hand[i].getRank() == card.getRank() and self.hand[i].getSuit() == card.getSuit():
               self.hand.pop(i)
               break
         
   def getHand(self):
       return self.hand
      
   def sortHand(self):
       for i in range(len(self.hand)-1):
           for j in range(len(self.hand)-1):
               card1 = self.hand[j]
               card2 = self.hand[j+1]              
               if((card1.getRank() > card2.getRank()) or ((card1.getRank() == card2.getRank()) and (card1.getSuit() > card.getSuit()))):                  
                   self.hand[j], self.hand[j+1] = self.hand[j+1], self.hand[j]
      

deck = Deck()
deck.shuffle()

player = Player("Charles")
for i in range(6):
   player.drawCard(deck)

print("The cards are: ")
hand = player.getHand()
for card in hand:
   print("{}{}".format(card.getSuit(),card.getRank()))

player.sortHand()
                                                                                                                                                                                                                                                                                                                                                                                                                               
print("Sorted hand is")  
hand = player.getHand()
for card in hand:
   print("{}{}".format(card.getSuit(),card.getRank()))


player.playCard(hand[1])  # remove the 2nd card from hand
print("The final cards after removal is:")  
hand = player.getHand()
for card in hand:
   print("{}{}".format(card.getSuit(),card.getRank()))

