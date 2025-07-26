import random
from DeckCards import DeckCards
from PlayerPlace import PlayerPlace
from PlayerUser import PlayerUser
from Player import Player


def start_game():
    name_list = ['Иван', 'Трофим', 'Петр', 'Николай', 'Иса', 'Хамид', 'Хулио']
    player_place = PlayerPlace()
    user = PlayerUser('Вы')
    player_place.main_player = user
    player_place.players_list.append(user)
    player_place.deck_cards = DeckCards()

    count_players = 0
    while count_players < 1:
        try:
            is_error = False
            count_players = int(input('Введите количество других игроков:'))
        except ValueError:
            is_error = True
            count_players = 0
            print('Необходимо ввести числовое значение!')

        if count_players < 1 and not is_error:
            print('Количество игроков должно быть больше одного!')

    # создание игроков
    for i in range(0, count_players):
        player = Player(name_list[i])
        player_place.players_list.append(player)

    # перемешать колоду
    player_place.deck_cards.mix_cards()
    # раздача карт
    player_place.dealing_cards()

    while True:
        for player_item in player_place.players_list:

            player_place.current_player = player_item
            index = player_place.players_list.index(player_item)
            if index == len(player_place.players_list) - 1:
                player_place.fights_back_player = player_place.players_list[0]
            else:
                player_place.fights_back_player = player_place.players_list[index + 1]
            # print(player_place.player_view())
            # print(player_place.fights_back_player.name)
            answer = player_place.start_player_game()
            if answer == 0:
                player_place.issuing_cards_to_players()

    # for player_item in player_place.players_list:
    #    player_place.current_player = player_item
    #   index = player_place.players_list.index(player_item)
    #   if index == len(player_place.players_list) - 1:
    #       player_place.fights_back_player = player_place.players_list[0]
    #  else:
    #      player_place.fights_back_player = player_place.players_list[index + 1]

    # print(player_place.player_view())
    # print('Колода:' + player_place.deck_cards.deck_cards_view())
    #  print('Ходит:' + player_item.name)
    #  print('Отбивается:' + player_place.fights_back_player.name)
    #  print('Карты на столе')
    # #first_step = True
    # if player_place.current_player != player_place.main_player:
    #    player_place.cards_on_table = player_item.make_first_move()
    #    print(player_place.cards_on_table_show())
    # else:
    #    user_action = input('Ваш ход:')
    #    player_place.player_item.get_cards_from_table(player_place.cards_on_table)
    # print('Ваши карты')
    # print(player_place.main_player.cart_view())
    # print('Ваши карты')
    # print(player_place.main_player.cart_view())
    ## player_item.make_move()
    # user_action = input('Ваш ход:')
    # player_place.print_border()


start_game()

# sentence = "This is a sample sentence."
# words = sentence.split()
# print(words)

# my_string = "apple#banana#cherry"
# fruits = my_string.split("#")
# print(fruits)
