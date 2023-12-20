# Favorite Card

import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards):
        dealt_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return dealt_cards

# Example card game: Draw three cards from a shuffled deck
if __name__ == "__main__":
    # Create a deck and shuffle it
    deck = Deck()
    deck.shuffle()

    # Draw three cards from the deck
    hand = deck.deal(3)

    # Display the drawn cards
    print("Your hand:")
    for card in hand:
        print(card)
