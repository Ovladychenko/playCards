class Player:
    # cards = []

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_cart(self, cart):
        self.cards.append(cart)

    def give_cart(self, cart):
        self.cards.remove(cart)

    def make_move(self):
        print('Ход бота')

    def find_min_cart(self, including_trump=False):
        if len(self.cards) == 0:
            return None

        priority = 50
        current_cart = None
        for cart_item in self.cards:
            if including_trump:
                if cart_item.priority < priority:
                    current_cart = cart_item
                    priority = cart_item.priority
            else:
                if cart_item.priority <= priority and not cart_item.is_trump:
                    current_cart = cart_item
                    priority = cart_item.priority

        return current_cart

    def similar_cards(self, cart, including_trump=False):
        if including_trump:
            filter_cards = list(filter(lambda cart_item: cart_item.priority == cart.priority,self.cards))
        else:
            filter_cards = list(filter(lambda cart_item: cart_item.priority == cart.priority and cart_item.is_trump !=True,self.cards))
        return filter_cards

    def make_first_move(self):
        cart = self.find_min_cart(self)
        return self.similar_cards(cart, False)

    def get_cards_from_table(self,cards_on_table):
        for cart_item in cards_on_table:
            self.cards.append(cart_item)
        cards_on_table.clear()


