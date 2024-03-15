# SAP Programming challenge: Card Game submission
# Author : Aditya Handrale

# library imports
import random # used to shuffling verification
import unittest # used for implementing tests


# Player class
# this class stores the player pile states and has the functions for discarding 
# and drawing cards
class Player:
    
    # initializing player variables
    def __init__(self, name):
        self.name =  name # name of the player
        self.draw_pile = [] # player's draw pile 
        self.discard_pile = [] #player's discard pile

    # draw function to draw a card from draw pile
    def draw(self):
        return draw_pile.pop
        




