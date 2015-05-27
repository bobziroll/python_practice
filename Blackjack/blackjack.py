"""
Problem:
Create a blackjack game in Python

Specifics:
Game should deal cards to a player.
Cards should have numbers and suits. Numbers will go from 1-13, suits will be spades, hearts, diamonds, or clubs.
Game should start by dealing 2 cards to the player.
Game should be able to determine value on the cards
    - 2-10 are valued by the card number
    - 11-13 should be worth 10
    - 1 should be worth either 1 or 11, depending

If cards add to 21 or less, return the sum of the cards
If the cards add to > 21, player should bust

Objects and classes we'll need:
    - Hand (will be made up of 2 or more cards)
    - Card (will have a value and a suit)
"""
import random


class Card(object):

    suits = ["spades", "hearts", "diamonds", "clubs"]

    def __init__(self):
        self.value = random.randint(1, 13)
        self.suit = random.choice(self.suits)

    def __str__(self):
        return "%s of %s" % (self.value, self.suit)

    def __add__(self, other):
        # TODO: Change Jack, Queen, and King values to a 10. Aces should be allowed to be 1 or 11.
        return self.value + other.value


class Hand(object):

    def __init__(self):
        self.card1 = Card()
        self.card2 = Card()
        self.cards = [self.card1, self.card2]

    def __str__(self):
        return "%s and %s" % (self.card1, self.card2)

    def hit_me(self):
        new_card = Card()
        self.cards.append(new_card)
        return new_card


hand = Hand()
print hand