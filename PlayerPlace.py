from DeckCards import DeckCards


class PlayerPlace:
    players_list = []
    main_player = None
    current_player = None
    fights_back_player = None
    cards_on_table = []
    deck_cards = None

    def dealing_cards(self):
        for i in range(6):
            for player_item in self.players_list:
                player_item.get_cart(self.deck_cards.give())

        # определение кто первый ходит
        cart = None
        priority = 0
        player = None
        for player_item in self.players_list:
            for card_item in player_item.cards:
                if card_item.suit == self.deck_cards.trump_suit and card_item.priority > priority:
                    cart = card_item
                    player = player_item
                    priority = card_item.priority

        if cart is not None:
            index = self.players_list.index(player)
            element = self.players_list.pop(index)
            self.players_list.insert(0, player)

    def player_view(self):
        result = ''
        for player_item in self.players_list:
            if player_item == self.current_player:
                result += '[' + player_item.name + ']' + ' '
            else:
                result += player_item.name + ' '
        return result

    def print_border(self):
        for i in range(150):
            print('=', end='')
        print(' ')

    def cards_on_table_show(self):
        result = ''
        index = 1
        for cart_item in self.cards_on_table:
            result += ' [' + str(index) + '] ' + cart_item.name + ' | '
            index += 1
        return result.rstrip()

    def start_player_game(self):
        pass