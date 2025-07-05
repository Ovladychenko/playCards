from DeckCards import DeckCards
class PlayerPlace:
    players_list = []
    main_player = None
    current_player = None

    def dealing_cards(self, deck_cards):
        for i in range(6):
            for player_item in self.players_list:
                player_item.get_cart(deck_cards.give())

        # определение кто первый ходит
        cart = None
        priority = 0
        player = None
        for player_item in self.players_list:
            for card_item in player_item.cards:
                if card_item.suit == deck_cards.trump_suit and card_item.priority > priority:
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