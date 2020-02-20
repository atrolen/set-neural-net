import random


class Card:
    def __init__(self, color, shape, fill, number):
        self.color = color
        self.shape = shape
        self.fill = fill
        self.number = number

    def show(self):
        print("{}, {}, {}, {}".format(self.color, self.shape, self.fill, self.number))


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for c in ["Red", "Green", "Purple"]:
            for s in ["squiggle", "oval", "diamond"]:
                for f in ["empty", "striped", "full"]:
                    for n in ["one", "two", "three"]:
                        self.cards.append(Card(c, s, f, n))

    def show(self):
        for v in self.cards:
            v.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]


deck = Deck()
deck.shuffle()
deck.show()
