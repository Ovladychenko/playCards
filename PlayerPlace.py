from DeckCards import DeckCards


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

    # def cards_on_table_show(self):
    #    result = ''
    # index = 1
    # for cart_item in self.cards_on_table:
    #    result += ' [' + str(index) + '] ' + cart_item.name + ' | '
    #    index += 1
    # return result.rstrip()

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

    def make_users_move(self):
        for player_item in self.players_list:
            if player_item != self.current_player and player_item != self.fights_back_player:
                print(f'Ищет карты {player_item.name}')
                for cart_item in self.cards_on_table_list:
                    cart_list = player_item.similar_cards(cart_item.get('cart'), False)
                    if len(cart_list) > 0:
                        print('Игрок ' + player_item.name + ' добавляет ' + self.get_list_cards_view(cart_list))
                        for cart_item_player in cart_list:
                            player_item.give_cart(cart_item_player)
                        self.cards_on_table_add_cards(cart_list)

    def cards_on_table_add_cards(self, cards):
        for cart_item in cards:
            self.cards_on_table.append(cart_item)
            cart_link = {'cart': cart_item, 'cart_link': None}
            self.cards_on_table_list.append(cart_link)

    @staticmethod
    def get_list_cards_view(cards):
        result = ''
        for cart_item in cards:
            result += cart_item.name + ' | '
        return result

    def processing_answer(self, answer):
        result = True
        if ' ' in answer:
            answer_list = answer.split()
            result = self.check_answer(answer_list)
        elif ',' in answer:
            answer_list = list()
            answer_list.append(answer)
            result = self.check_answer(answer_list)
        return result

    def check_answer(self, answer_list):
        is_error = False
        for answer_item in answer_list:
            if not ',' in answer_item:
                return False
            answer_array = answer_item.split(',')
            # получаем карту на столе
            cart_dict = self.cards_on_table_list[int(answer_array[0]) - 1]
            cart_table = cart_dict.get('cart')
            # получаем карту игрока
            cart_user = self.main_player.cards[int(answer_array[1]) - 1]
            if (cart_user.priority > cart_table.priority and cart_user.suit == cart_table.suit) or (
                    cart_user.is_trump and not cart_table.is_trump) or (
                    (cart_user.is_trump and cart_table.is_trump) and (cart_user.priority > cart_table.priority)
            ):
                cart_dict['cart_link'] = cart_user
                self.main_player.give_cart(cart_user)
            else:
                print('Карта ' + cart_user.name + ' не может бить карту ' + cart_table.name)

        return is_error

    # Проверка биты ли все карты на столе
    def is_card_bits(self):
        index = 0
        for cart_item in self.cards_on_table_list:
            if cart_item.get('cart_link') is not None:
                index += 1
        return len(self.cards_on_table_list) == index

    def cards_on_table_count(self):
        result = 0
        for cart_item in self.cards_on_table_list:
            if cart_item.get('cart') is not None:
                result += 1
        return result

    def card_for_table_validate(self, card_user):
        result = False
        for card_dict in self.cards_on_table_list:
            if card_dict.get('cart').priority == card_user.priority:
                result = True
                break
        return result

    def issuing_cards_to_players(self):
        for player_item in self.players_list:
            if len(player_item.cards) < 6:
                need_cards = 6 - len(player_item.cards)
                for i in range(need_cards):
                    player_item.get_cart(self.deck_cards.give())

    def move_main_player(self, answer, first_step=False):
        answer_array = list()
        if ',' in answer:
            answer_array = answer.split(',')
        else:
            answer_array.append(answer)

        for answer_item in answer_array:
            cart_user = self.main_player.cards[int(answer_item) - 1]
            if first_step:
                if self.cards_on_table_count() != 0:
                    if self.cards_on_table_list[0].get('cart').priority != cart_user.priority:
                        print(f'Карта {cart_user.name} не может ходить')
                        continue
            else:
                if not self.card_for_table_validate(cart_user):
                    print(f'Карта {cart_user.name} не может ходить')
                    continue

            cart_link = {'cart': cart_user, 'cart_link': None}
            self.cards_on_table_list.append(cart_link)
            self.main_player.give_cart(cart_user)
            # cards
        # cart_link = {'cart': cart_item, 'cart_link': None}
        # self.cards_on_table_list.append(cart_link)

    # def move_player(self):
    #    for card_dict in self.cards_on_table_list:
    #        cart_table = card_dict.get('cart')

    def start_player_game(self):
        first_step = True
        self.cards_on_table.clear()
        self.cards_on_table_list.clear()
        while True:
            print(self.player_view())
            print('Колода:' + self.deck_cards.deck_cards_view())
            print(f'Ходит: {self.current_player.name} у игрока {len(self.fights_back_player.cards)} карт ')
            print(f'Отбивается: {self.fights_back_player.name}  ')

            if first_step:
                if self.current_player != self.main_player:
                    self.cards_on_table_add_cards(self.current_player.make_first_move())
                    self.make_users_move()
            else:
                self.make_users_move()
            print('Карты на столе')
            print(self.cards_on_table_show())
            print('Ваши карты')
            print(self.main_player.cart_view())
            if self.current_player == self.main_player:
                answer = input('Ваш ход [карты через запятую]:')
                if answer == '+':
                    if self.is_card_bits():
                        print('Отбой')
                        return 0
                    else:

                        pass
                else:
                    self.move_main_player(answer, first_step)
                    self.make_users_move()
                    self.current_player.move_player(self.cards_on_table_list)
            else:
                answer = input('Ваш ход [На столе, Ваша карта]:')
                if answer == '+':
                    continue
                elif answer == '-':
                    self.main_player.get_cards_from_table(self.cards_on_table)
                    return 0
                else:
                    result = self.processing_answer(answer)
            # if self.is_card_bits() and self.current_player == self.main_player:
            #    print('Отбой карт, ход переходит следующему игроку!')
            #    return 0
            first_step = False
            self.print_border()
