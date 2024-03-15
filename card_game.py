# SAP Programming challenge: Card Game submission
# Author : Aditya Handrale

# Library imports
from math import floor # used for improved Fisher-Yates algorithm
import random # used to shuffling verification
import unittest # used for implementing tests


# Function used to shuffle the cards
# python's random.shuffle() internally used fisher-yates algorithm with O(n)
# but this improved Fisher-Yates algorithm with O(n-1) (credit : https://gist.github.com/JenkinsDev/1e4bff898c72ec55df6f)
# card : list of cards
def improved_fisher_yates_shuffle(deck):
    amount_to_shuffle = len(deck)
    while amount_to_shuffle>1:
        i = int(floor(random() * amount_to_shuffle))
        amount_to_shuffle -= 1
        


    for i in range(len(deck)-1, 0, -1):
        j = random.randint(0, i)
        deck[i], deck[j] = deck[j], deck[i]


# Player class
# this class stores the player pile states and has the functions for discarding 
# and drawing cards
class Player:
    
    # initializing player variables
    # name : string name
    def __init__(self, name):
        self.name =  name # name of the player
        self.draw_pile = [] # player's draw pile list 
        self.discard_pile = [] #player's discard pile list

    # draw function to draw a card from draw pile
    def draw(self):
        # first, check if draw pile empty
        if len(self.draw_pile) == 0 :
            # shuffle and add the discard pile to the draw pile
            # TODO shuffle function () 
            self.draw_pile.extend(self.discard_pile)
            # clear the discard pile to avoid card duplicaiton
            self.draw_pile.clear()

        # popping a card from the top of draw_pile
        return self.draw_pile.pop(0)
        
    # function for discarding a card, i.e. adding it to the discard pile
    # card : card object passed from draw pile
    def discard(self, card):
        self.discard_pile.append(card)



# Deck class
# this class stores deck of cards and has related functions like 
# shuffle (Fisher-Yates method), generate and draw
class Deck:
    def __init__(self):
        # list to store the cards in a deck
        self.cards = []

    # generate the cards according to specifications
    def generate(self):
        for i in range(4):
            for j in range(1,11):
                self.cards.append()
    
    def shuffle(self):
        # TODO implement shuffle outside class
        self.cards = self.cards
    
    # function used to draw a card on top of the deck
    def draw(self):
        return self.cards.pop(0)
    






