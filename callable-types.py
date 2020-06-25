# Not only are Python functions real objects, but arbitrary Python objects may also be made to behave like functions. Implementing a __call__ instance method is all it takes.

import random


class BingoCage:
    def __init__(self, items):
        self.items = list(items)
        random.shuffle(self.items)

    def pick(self):
        try:
            return self.items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


bingo = BingoCage(range(3))
print(bingo.pick())
print(bingo())  # __call__ makes it callable
print(callable(bingo))
