# SAP Programming challenge: Card Game submission
# Card game emulation in python, makes use of the classes Card, Deck, Player and Game
# Author : Aditya Handrale

# Library imports
from math import floor # used for improved Fisher-Yates algorithm
import random # used to shuffling verification
import unittest # used for implementing tests
from art import * # external library used to print ASCII art


# TODO : Add various TODO s for future work features
# TODO : Show discard piles and draw piles spereately
# Used for verbose debug mode logging
DEBUG = True

# Function used to shuffle the cards
# python's random.shuffle() internally used Fisher-Yates algorithm with O(n)
# but this improved Fisher-Yates algorithm works with O(n-1) (credit : https://gist.github.com/JenkinsDev/1e4bff898c72ec55df6f)
# since this function gets object passed by reference, and lists are mutable in python, changes will reflect in original object
# deck : list of cards
def improved_fisher_yates_shuffle(deck):
    amount_to_shuffle = len(deck)
    while amount_to_shuffle>1:
        i = int(floor(random.random() * amount_to_shuffle))
        amount_to_shuffle -= 1
        deck[i], deck[amount_to_shuffle] = deck[amount_to_shuffle], deck[i]


# Verbose logging function used for debugging, only functions if DEBUG = True 
def log(message):
    if DEBUG:
        print(f"[LOG]: "+ message)


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
        self.total_cards = 20 # for tracking the score

    # draw function to draw a card from draw pile
    def draw(self):
        # first, check if draw pile empty
        if not self.draw_pile:
            # now we need to shuffle discard pile and add it to draw
            # so first we check if discard pile is also empty
            if not self.discard_pile:
                return None # no cards left to draw, end the game
            
            # if discard pile does have cards available to draw,
            # shuffle and add the discard pile to the draw pile
            improved_fisher_yates_shuffle(self.discard_pile)
            self.draw_pile.extend(self.discard_pile)
            # clear the discard pile to avoid card duplicaiton
            self.discard_pile.clear()

        # popping a card from the top of draw_pile
        return self.draw_pile.pop(0)
        
    # function for discarding a card, i.e. adding it to the discard pile
    # card : card object passed from draw pile
    def discard(self, card):
        self.discard_pile.append(card)




# Card class
# this class represents an individual card and dunder functions for setting and getting values
# value : int value of the card
class Card:
    # initializing a card like Card(10) to create card with 10 value 
    def __init__(self,value):
        self.value = value
    # returning a string represenation as value of card for easier printing
    def __str__(self):
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
                self.cards.append(Card(j)) # initialize the card object and add to cards list
    
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


    # function that emulates a player turn, i.e. executes a single round of the game
    def play_round(self):
        # draw a card for each player from their respective draw_piles
        p1_card = self.p1.draw()
        p2_card = self.p2.draw()

        # check if any player couldn't draw a card
        if p1_card is None or p2_card is None:
            print("No more cards left to draw. Game over!")
            return

        # TODO add fancy console log prints
        print(f"{self.p1.name} [Player 1] draws a {p1_card}! [Score : {self.p1.total_cards}]\n{self.p2.name} [Player 2] draws a {p2_card}! [Score : {self.p2.total_cards}]")

        
        # check if player 1 won the round
        if p1_card.value > p2_card.value:
            print(f"{self.p1.name} wins this round!\n")

            # add both the cards to player 1 discard pile, since they won this round
            self.p1.discard(p1_card)
            self.p1.discard(p2_card)

            # update the score, as winner gets their old card + 1 new card from loser back
            self.p1.total_cards += 1
            self.p2.total_cards -= 1


        # else check if player 2 won the round
        elif p2_card.value > p1_card.value:
            print(f"{self.p2.name} wins this round!\n")

            # add both the cards to player 2 discard pile, since they won this round
            self.p2.discard(p1_card)
            self.p2.discard(p2_card)

            # update the score, as winner gets their old card + 1 new card from loser back
            self.p2.total_cards += 1
            self.p1.total_cards -= 1
        # this means both player drew the same value card and its a tie
        else:
            print("Its a tie! No winner this round")
            self.handle_tie(tied_cards=[p1_card,p2_card])


    # this recursive function occurs when there is a tie, and keeps calling itself for further ties, while storing all previous tie round cards
    # so that winner after consecutive ties gets all the previous cards, so as to avoid a stalemate
    # tied_cards : list of cards that stores all the previously tied cards, recursively passed to handle_tie
    def handle_tie(self, tied_cards=None):
        print("Resolving the tie...")

        # if handle tie called non recursively (for the first time), create a tied_cards list first 
        if tied_cards is None:
            tied_cards = []

        # draw 2 new cards for each player and add them to tied_cards, as tied_cards list will be awarded to player who wins after consecutive ties
        tied_cards.extend([self.p1.draw(), self.p2.draw()])
        # Check if No e is present in tied_cards, meaning a player has exhausted their cards
        # and we should end the game
        if None in tied_cards:
            return

        # now take each of the players newly drawn cards, which were stored in tied_cards
        # to see who wins this round
        last_card_p1 = tied_cards[-2]
        last_card_p2 = tied_cards[-1]

        # update the total_cards
        # self.p1.total_cards -= 1
        # self.p2.total_cards -= 1


        print(f"{self.p1.name} [Player 1] draws a {last_card_p1}! \n{self.p2.name} [Player 2] draws a {last_card_p2}!")


        # check the winning conditions again to see who wins the tie
        # if player 1 wins 
        if last_card_p1.value > last_card_p2.value:
            print(f"{self.p1.name} [Player 1] wins the tiebreaker, and recieves the last {len(tied_cards)} cards!\n")
            
            # update the total_cards
            self.p1.total_cards += int(len(tied_cards)/2)
            self.p2.total_cards -= int(len(tied_cards)/2)

            self.p1.discard_pile.extend(tied_cards) # add the tied cars list to player 1 discard pile
        # if player 2 wins
        elif last_card_p1.value < last_card_p2.value:
            print(f"{self.p2.name} [Player 2] wins the tiebreaker, and recieves the last {len(tied_cards)} cards!\n")
           
            # update the total_cards 
            self.p2.total_cards += int(len(tied_cards)/2)
            self.p1.total_cards -= int(len(tied_cards)/2)

            self.p2.discard_pile.extend(tied_cards) # add the tied cars list to player 2 discard pile
        # if its a tie again, call the handle_tie function again and pass the tied_cards list which contains the previously tied cards
        else:
            print("Uh oh! Another tie! Resolving...")
            print(f"{self.p1.name} (Player 1) draws a {last_card_p1}! [Score : {self.p1.total_cards}]\n{self.p2.name} (Player 2) draws a {last_card_p2}! [Score : {self.p2.total_cards}]")

            self.handle_tie(tied_cards)  # Recursively call handle_tie() with the same tied_cards list
    


    # this function is responsible for the main gameplay loop
    def play_game(self):
        print("\n")
        # keep playing rounds till any/both player's draw pile is empty
        while True:

            # if both platyers have no more cards left to draw, break gameplay loop
            if not self.p1.draw_pile and not self.p1.discard_pile:
                print("Both players have exhausted their cards, Game Over!")
                break

            # if both players have drawable cards, play the round
            self.play_round()

            # after playing a round, check if any player exhausted their cards
            # if one of the players has no more cards left to draw, break gameplay loop
            # check if player 1 has exhausted their cards
            if not self.p1.draw_pile and not self.p1.discard_pile:
                print(f"{self.p1.name} [Player 1] exhausted their cards and is unable to draw any more cards, Game Over!")
                break # end the gameplay loop
            # check if player 2 has exhausted their cards
            if not self.p2.draw_pile and not self.p2.discard_pile:
                print(f"{self.p2.name} [Player 2] exhausted their cards and is unable to draw any more cards, Game Over!")
                break # end the gameplay loop
        
        # print the final scores
        print(f"\nFinal scores:\n{self.p1.name} Score : {self.p1.total_cards}")
        print(f"{self.p2.name} Score : {self.p2.total_cards}")

        # After the gameplay loop is finished,
        # check for who won the whole game
        

        # if player 1's discard pile is greater, they win
        if len(self.p1.discard_pile) > len(self.p2.discard_pile):
            print(f"[Player 1] {self.p1.name} wins the game!")

        # if player 2's discard pile is greater, they win
        elif len(self.p1.discard_pile) < len(self.p2.discard_pile):
            print(f"[Player 2] {self.p2.name} wins the game!\n")

        # if both discard piles are the same length, its a tie
        else:
            print("It's a tie!\n")
        
        tprint(f"\n\n GGWP!", font="crawford") # Used for ASCII art


    
# main function responsible for getting the player names, setting up and running the game
def main():
    tprint("\n\n SAP Card Game", font="crawford") # Used for ASCII art
    print("Copyright © 2024 Aditya Handrale\n ")

    print("\n#################################")
    print("# Welcome to the SAP Card Game! #")
    print("#################################\n")

    player1_name = input("Please enter player 1 Name : ")
    player2_name = input("Please enter player 2 Name : ")

    game_instance = Game(player1_name.upper(), player2_name.upper())
    game_instance.initialize_game()
    game_instance.play_game()

if __name__ == "__main__":
    main()