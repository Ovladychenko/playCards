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

    def make_users_move(self):
        for player_item in self.players_list:
            if player_item != self.current_player and player_item != self.fights_back_player:
                for cart_item in self.cards_on_table:
                    cart_list = player_item.similar_cards(cart_item, False)
                    if len(cart_list) > 0:
                        print('Игрок ' + player_item.name + ' добавляет ' + self.get_list_cards_view(cart_list))
                        for cart_item_player in cart_list:
                            player_item.give_cart(cart_item_player)
                        self.cards_on_table_add_cards(cart_list)

    def cards_on_table_add_cards(self, cards):
        for cart_item in cards:
            self.cards_on_table.append(cart_item)

    @staticmethod
    def get_list_cards_view(cards):
        result = ''
        for cart_item in cards:
            result += cart_item.name + ' | '
        return result

    def start_player_game(self):
        first_step = True
        self.cards_on_table.clear()
        while True:
            print(self.player_view())
            print('Колода:' + self.deck_cards.deck_cards_view())
            print('Ходит:' + self.current_player.name)
            print('Отбивается:' + self.fights_back_player.name)
            # print('Карты на столе')
            # print(player_place.cards_on_table_show())
            # print('Ваши карты')
            # print(self.main_player.cart_view())

            if first_step:
                if self.current_player == self.main_player:  # Ход реального игрока
                    pass
                else:
                    self.cards_on_table_add_cards(self.current_player.make_first_move())
                    self.make_users_move()
            else:
                pass
            print('Карты на столе')
            print(self.cards_on_table_show())
            print('Ваши карты')
            print(self.main_player.cart_view())
            input('Ваш ход:')
            first_step = False
            self.print_border()
