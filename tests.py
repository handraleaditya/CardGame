# Tests file for the card game
# Author : Aditya Handrale

import unittest # using the pytohns testing module
from card_game import Card, Deck, Player, Game # Deck, Player, Card, Game class


class TestDeck(unittest.TestCase):
    
    # New deck should contain 40 cards test
    def test_new_deck_has_40_cards(self):
        # initialize new deck
        deck = Deck()
        deck.generate()
        # assert if it has 40 cards
        self.assertEqual(len(deck.cards), 40, "New deck should have 40 cards")

    # Shuffle function shuffles a deck
    def test_shuffle_function_shuffles(self):
        # initialize a new deck
        deck = Deck()
        deck.generate()
        # create copy of original deck
        original_deck = deck.cards.copy()
        # shuffle the deck
        deck.shuffle()
        # assert that shuffled deck is not equal to original deck
        self.assertNotEqual(deck.cards, original_deck, "New deck needs to be shuffled")

    # When draw pile is empty, discard pile should get shuffled into draw pile
    def test_empty_draw_pile(self):
        # initialize the Player
        p1 = Player("test_player") 
        # initialize empty draw pile
        p1.draw_pile = []
        # initialize discard pile with 5 cards
        p1.discard_pile = [Card(i) for i in range(0,5)]
        initial_discard_pile = p1.discard_pile.copy()
        # try to draw a card
        drawn_card = p1.draw()
        # asset if draw pile has 4 cards
        self.assertNotEqual(p1.draw_pile, [], "Draw pile should not be empty after shuffling")
        self.assertEqual(p1.discard_pile, [], "Discard pile should be empty after shuffling")
        # we pop a card from draw pile when draw() is called, hence +1
        self.assertEqual(len(p1.draw_pile) + 1, len(initial_discard_pile), "Draw pile should contain all cards from the initial discard pile")

    # When comparing two cards, card with higher value should win
    def test_higher_card_wins(self):
        # initialize test scenario
        game = Game("test_player_1", "test_player_2")
        p1 = game.p1
        p2 = game.p2
        p1_card = Card(7)  # Higher card for player 1
        p2_card = Card(3)  # Lower card for player 2
        # set up draw piles
        p1.draw_pile = [p1_card]
        p2.draw_pile = [p2_card]
        # act
        game.play_round()
        # assert if player 1 with higher value card wins
        self.assertEqual(len(p1.discard_pile), 2, "Player 1 should have 2 cards in their discard pile after winning")
        self.assertEqual(len(p2.discard_pile), 0, "Player 2 should have 0 cards in their discard pile after losing")

    # When comparing two same value cards, winner next round should win 4 cards
    def test_tiebreaker_wins_4_cards(self):
        # initiailize the game
        game = Game("test_player_1", "test_player_2")
        p1 = game.p1
        p2 = game.p2
        # rigging the cards according to test conditions
        p1_card = Card(5)
        p2_card = Card(5)
        p1_next_card = Card(9)
        p2_next_card = Card(1)
        # set up draw piles with cards for tie, and next so that player 1 wins
        p1.draw_pile = [p1_card, p1_next_card]
        p2.draw_pile = [p2_card, p2_next_card]
        game.play_round()  # perform tiebreaker round
        # assert if player 1 won 4 cards
        self.assertEqual(len(p1.discard_pile), 4, "Player 1 should have 4 cards in their discard pile after winning tiebreaker")
        self.assertEqual(len(p2.discard_pile), 0, "Player 2 should have 0 card in their discard pile after losing tiebreaker")



if __name__ == "__main__":
    unittest.main()