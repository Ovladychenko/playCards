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
            filter_cards = list(filter(lambda cart_item: cart_item.priority == cart.priority, self.cards))
        else:
            filter_cards = list(
                filter(lambda cart_item: cart_item.priority == cart.priority and cart_item.is_trump != True,
                       self.cards))
        return filter_cards

    def make_first_move(self):
        print(f'{self.name} ищет карты')
        cart = self.find_min_cart(self)
        print(f'минимальная карта {cart.name}')
        card_list = self.similar_cards(cart, False)
        if len(card_list) == 0:
            card_list.append(cart)

        for card_item in card_list:
            self.give_cart(card_item)
        return card_list

    def get_cards_from_table(self, cards_on_table_list):
        # for cart_item in cards_on_table:
        #    self.cards.append(cart_item)
        # cards_on_table.clear()
        for card_dict in cards_on_table_list:
            if card_dict.get('cart') is not None:
                self.cards.append(card_dict.get('cart'))
            if card_dict['cart_link'] is not None:
                self.cards.append(card_dict['cart_link'])
        cards_on_table_list.clear()

    def move_player(self, cards_on_table_list):
        for card_dict in cards_on_table_list:
            card_table = card_dict.get('cart')
            if card_dict['cart_link'] != None:
                continue

            for card_item in self.cards:
                if card_item.priority > card_table.priority and card_item.suit == card_table.suit:
                    card_dict['cart_link'] = card_item
                    self.give_cart(card_item)
                    print(f'Игрок отбивает карту {card_table.name} картой {card_item.name}')
                    break

                if (card_item.priority > card_table.priority and card_item.is_trump
                        and not card_table.is_trump):
                    card_dict['cart_link'] = card_item
                    self.give_cart(card_item)
                    print(f'Игрок отбивает карту {card_table.name} картой {card_item.name}')
                    break
