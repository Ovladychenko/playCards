from Player import Player


class PlayerUser(Player):
    def cart_view(self):
        result = ''
        index = 1
        for cart_item in self.cards:
            result += ' [' + str(index) + '] ' + cart_item.name + ' | '
            index += 1

        result += ' [+]  Пас'
        result += ' [-]  Забрать'
        return result

    def processing_answer(self, answer, player_place):
        result = True
        if ' ' in answer:
            answer_list = answer.split()
            result = self.__check_answer(answer_list, player_place)
        elif ',' in answer:
            answer_list = list()
            answer_list.append(answer)
            result = self.__check_answer(answer_list, player_place)
        return result

    def __check_answer(self, answer_list, player_place):
        is_error = False
        for answer_item in answer_list:
            if not ',' in answer_item:
                return False
            answer_array = answer_item.split(',')
            # получаем карту на столе
            cart_dict = player_place.cards_on_table_list[int(answer_array[0]) - 1]
            cart_table = cart_dict.get('cart')
            # получаем карту игрока
            cart_user = player_place.main_player.cards[int(answer_array[1]) - 1]
            if (cart_user.priority > cart_table.priority and cart_user.suit == cart_table.suit) or (
                    cart_user.is_trump and not cart_table.is_trump) or (
                    (cart_user.is_trump and cart_table.is_trump) and (cart_user.priority > cart_table.priority)
            ):
                cart_dict['cart_link'] = cart_user
                player_place.main_player.give_cart(cart_user)
            else:
                print('Карта ' + cart_user.name + ' не может бить карту ' + cart_table.name)

        return is_error

    def move_main_player(self, answer, player_place, first_step=False):
        answer_array = list()
        if ',' in answer:
            answer_array = answer.split(',')
        else:
            answer_array.append(answer)

        for answer_item in answer_array:
            cart_user = player_place.main_player.cards[int(answer_item) - 1]
            if first_step:
                if player_place.__cards_on_table_count() != 0:
                    if player_place.cards_on_table_list[0].get('cart').priority != cart_user.priority:
                        print(f'Карта {cart_user.name} не может ходить')
                        continue
            else:
                if not player_place.__card_for_table_validate(cart_user):
                    print(f'Карта {cart_user.name} не может ходить')
                    continue

            cart_link = {'cart': cart_user, 'cart_link': None}
            player_place.cards_on_table_list.append(cart_link)
            player_place.main_player.give_cart(cart_user)
