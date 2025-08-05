from DeckCards import DeckCards
from Player import Player

class PlayerPlace:
    players_list = []
    main_player = None
    current_player = None
    fights_back_player = None
    cards_on_table = []
    deck_cards = None
    cards_on_table_list = []

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

    def __player_view(self):
        result = ''
        for player_item in self.players_list:
            if player_item == self.current_player:
                result += '[' + player_item.name + ']' + ' '
            else:
                result += player_item.name + ' '
        return result

    def __print_border(self):
        for i in range(150):
            print('=', end='')
        print(' ')

    def cards_on_table_show(self):
        result = ''
        index = 1
        for cart_item in self.cards_on_table_list:
            name = cart_item.get('cart').name
            if cart_item.get('cart_link') != None:
                name = name + ' / ' + cart_item.get('cart_link').name

            result += ' [' + str(index) + '] ' + name + ' | '
            index += 1
        return result.rstrip()

    def cards_on_table_add_cards(self, cards):
        for cart_item in cards:
            # self.cards_on_table.append(cart_item)
            cart_link = {'cart': cart_item, 'cart_link': None}
            self.cards_on_table_list.append(cart_link)

    @staticmethod
    def get_list_cards_view(cards):
        result = ''
        for cart_item in cards:
            result += cart_item.name + ' | '
        return result

    # Проверка биты ли все карты на столе
    def __is_card_bits(self):
        index = 0
        for cart_item in self.cards_on_table_list:
            if cart_item.get('cart_link') is not None:
                index += 1
        return len(self.cards_on_table_list) == index

    def __cards_on_table_count(self):
        result = 0
        for cart_item in self.cards_on_table_list:
            if cart_item.get('cart') is not None:
                result += 1
        return result

    def __card_for_table_validate(self, card_user):
        result = False
        for card_dict in self.cards_on_table_list:
            if card_dict.get('cart').priority == card_user.priority:
                result = True
                break
            if card_dict.get('cart_link') is not None:
                if card_dict.get('cart_link').priority == card_user.priority:
                    result = True
                    break

        return result

    def issuing_cards_to_players(self):
        for player_item in self.players_list:
            if len(player_item.cards) < 6:
                need_cards = 6 - len(player_item.cards)
                for i in range(need_cards):
                    player_item.get_cart(self.deck_cards.give())

    def start_player_game(self):
        first_step = True
        # self.cards_on_table.clear()
        self.cards_on_table_list.clear()
        while True:
            print(self.__player_view())
            print('Колода:' + self.deck_cards.deck_cards_view())
            print(f'Ходит: {self.current_player.name} у игрока {len(self.fights_back_player.cards)} карт ')
            print(f'Отбивается: {self.fights_back_player.name}  ')

            if first_step:
                if self.current_player != self.main_player:
                    self.cards_on_table_add_cards(self.current_player.make_first_move())
                    Player.make_users_move(self)
            else:
                Player.make_users_move(self)
            print('Карты на столе')
            print(self.cards_on_table_show())
            print('Ваши карты')
            print(self.main_player.cart_view())
            if self.current_player == self.main_player:
                answer = input('Ваш ход [карты через запятую]:')
                if answer == '+':
                    if self.__is_card_bits():
                        print('Отбой')
                        self.__print_border()
                        return 0
                    else:
                        # забрать карты игрока
                        print(f' {self.current_player.name} забирает карты со стола')
                        self.current_player.get_cards_from_table(self.cards_on_table_list)
                        return 0
                else:
                    self.main_player.move_main_player(answer,self, first_step)
                    Player.make_users_move(self)
                    self.current_player.move_player(self.cards_on_table_list)
            else:
                answer = input('Ваш ход [На столе, Ваша карта]:')
                if answer == '+':
                    if self.__is_card_bits() and self.fights_back_player != self.main_player:
                        return 0
                    else:
                        continue
                elif answer == '-':
                    self.main_player.get_cards_from_table(self.cards_on_table_list)
                    return 0
                else:
                    result = self.main_player.processing_answer(answer, self)
            # if self.is_card_bits() and self.fights_back_player == self.main_player:
            #    print('Отбой карт, ход переходит следующему игроку!')
            #    return 0
            first_step = False
            self.__print_border()
