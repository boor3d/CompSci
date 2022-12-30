# Create a Ride the Bus Game That Replicates the Drinking Game

import random

# Create a Card Class that Contains all Cards in a Standard 52-card deck 

class Card:
    
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit
        self.color = 'black' if suit.endswith(("Spades", "Clubs")) else 'red'

    def show(self):
        return f'{self.value} of {self.suit}'


class Deck:

    def __init__(self):
        self.cards = []
        self.build()
        self.shuffle()

    def build(self):
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        for s in suits:
            for v in range(1,14):
                if v == 1:
                    v = "A"
                elif v == 11:
                    v = "J"
                elif v == 12:
                    v = "Q"
                elif v == 13:
                    v = "K"
                else:
                    pass
                self.cards.append(Card(s, v))

    def show_deck(self):
        for c in self.cards:
            print(c.show())

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw_card(self):
        self.cards.pop()


# class Player:
#     def __init__(self, name):
#         self.name = name




deck = Deck()
deck.show_deck()



round = 0
