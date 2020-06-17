import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self.cards = [Card(rank, suit)
                      for suit in self.suits for rank in self.ranks]

    # allows for len()
    def __len__(self):
        return len(self.cards)

    # this makes it iterable, sliceable, and reversed()
    def __getitem__(self, position):
        return self.cards[position]


deck = FrenchDeck()
print(len(deck))

# pick random
print(choice(deck))

# __contains__ method implements in operator but if doesn't exist it will complete a sequential scan
print(Card('Q', 'hearts') in deck)
