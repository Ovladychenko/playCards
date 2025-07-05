class Player:
    # cards = []

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_cart(self, cart):
        self.cards.append(cart)

    def make_move(self):
        pass
