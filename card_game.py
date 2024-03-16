# SAP Programming challenge: Card Game submission
# Author : Aditya Handrale

# Library imports
from math import floor # used for improved Fisher-Yates algorithm
import random # used to shuffling verification
import unittest # used for implementing tests

# TODO : Add various TODO s for future work features

# Function used to shuffle the cards
# python's random.shuffle() internally used fisher-yates algorithm with O(n)
# but this improved Fisher-Yates algorithm with O(n-1) (credit : https://gist.github.com/JenkinsDev/1e4bff898c72ec55df6f)
# since this function gets object passed by reference, and lists are mutable in python, changes will reflect in original object
# deck : list of cards
def improved_fisher_yates_shuffle(deck):
    amount_to_shuffle = len(deck)
    while amount_to_shuffle>1:
        i = int(floor(random.random() * amount_to_shuffle))
        amount_to_shuffle -= 1
        deck[i], deck[amount_to_shuffle] = deck[amount_to_shuffle], deck[i]


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
        self.score = 0 # for tracking the score

    # draw function to draw a card from draw pile
    def draw(self):
        # first, check if draw pile empty
        if len(self.draw_pile) == 0 :
            # shuffle and add the discard pile to the draw pile
            improved_fisher_yates_shuffle(self.discard_pile)
            self.draw_pile.extend(self.discard_pile)
            # clear the discard pile to avoid card duplicaiton
            self.draw_pile.clear()

        # popping a card from the top of draw_pile
        return self.draw_pile.pop(0)
        
    # function for discarding a card, i.e. adding it to the discard pile
    # card : card object passed from draw pile
    def discard(self, card):
        self.discard_pile.append(card)

    # this functions keeps track of the score of the player
    def score(self):
        # current score is calculated as no. of cards in draw + discard pile
        self.score = len(self.discard_pile) + len(self.draw_pile)
        return self.score



# Card class
# this class represents an individual card and dunder functions for setting and getting values
# value : int value of the card
class Card:
    # initializing a card like Card(10) to create card with 10 value 
    def __init__(self,value):
        self.value = value
    # returning a string represenation as value of card for easier printing
    def __str__(self,value):
        return str(self.value)
    
# Deck class
# this class represents deck of cards and has related functions like 
# shuffle (Fisher-Yates method), generate and draw
class Deck:
    def __init__(self):
        # list to store all the cards in a deck
        self.cards = []

    # generate the cards according to specifications
    def generate(self):
        for i in range(4): # each card should repeat 4 times
            for j in range(1,11): # each card must hae value 1-10
                self.cards.append(Card(i)) # initialize the card object and add to cards list
    
    def shuffle(self):
        improved_fisher_yates_shuffle(self.cards)
        self.cards = self.cards
    
    # function used to draw a card on top of the deck
    def draw(self):
        return self.cards.pop(0)
    

# Game class
# this class is used to manage the game, has functions to initialize the game, handle game logic
class Game:
    # Initialize Player and Deck objects
    def __init__(self, player1_name, player2_name):
        # initialize the player objects using the provided names, p1 is abbrevation for player 1
        self.p1 = Player(player1_name)
        self.p2 = Player(player2_name)
        # initialize the deck
        self.deck = Deck()

    def initialize_game(self):
        # populate the deck with Card objects
        self.deck.generate()
        # shuffle the newly generated deck
        self.deck.shuffle()
        # distribute the cards between the two players
        self.p1.draw_pile = self.deck.cards[:20] # player 1 gets first 20 cards
        self.p2.draw_pile = self.deck.cards[20:] # player 2 gets the last 20


    # function that emulates a player turn
    def play_round(self):
        # draw a card for each player from their respective draw_piles
        p1_card = self.p1.draw()
        p2_card = self.p2.draw()

        # TODO add fancy console log prints
        print(f"{self.p1.name}(Player 1) draws a {p1_card}! [Score : {self.p1.score()}]\n{self.p2.name} (Player2) draws a {p2_card} [Score : {self.p2.score()}]")
        
        # check if player 1 won the round
        if p1_card.value > p2_card.value:
            print(f"{self.p1.name} wins this round!")
            # add both the cards to player 1 discard pile, since they won this round
            self.p1.add_to_discard_pile(p1_card)
            self.p1.add_to_discard_pile(p2_card)
        # else check if player 2 won the round
        if p2_card.value > p1_card.value:
            print(f"{self.p1.name} wins this round!")
            # add both the cards to player 2 discard pile, since they won this round
            self.p1.add_to_discard_pile(p1_card)
            self.p1.add_to_discard_pile(p2_card)










