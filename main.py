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
    deck_cards = DeckCards()

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
    deck_cards.mix_cards()
    # раздача карт
    player_place.dealing_cards(deck_cards)

    # while True:
    #    for player_item in player_place.players_list:
    #        print(player_item.name)

    for player_item in player_place.players_list:
        player_place.current_player = player_item
        print(player_place.player_view())
        player_place.print_border()
        print(player_place.main_player.cart_view())
        player_place.print_border()
        input('')

start_game()
