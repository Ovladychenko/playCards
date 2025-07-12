import random


class DeckCards:
    "Класс колода карт"
    cards = []
    suits = ['Бубен', 'Треф', 'Черва', 'Пика']
    name_high = ['Валет', 'Дама', 'Король', 'Туз']
    trump_suit = ""
    last_card = ""

    def __init__(self):
        # "Создание колоды карт"
        self.cards.clear()

        for suit in self.suits:
            priority = 0
            for i in range(6, 11):
                priority += 1
                # print(str(i) + ' (' + suit + ')')
                card = Card(str(i) + ' (' + suit + ')', priority, suit, i, False)
                self.cards.append(card)

            # add higth cards
            for name in self.name_high:
                priority += 1
                card = Card(name + ' (' + suit + ')', priority, suit, i, True)
                # print(name + ' (' + suit + ')')
                self.cards.append(card)

    def mix_cards(self):
        # перемешать карты
        for i in range(10):
            temp_list_cards = self.cards.copy()
            self.cards.clear()

            while len(temp_list_cards) > 0:
                find_item = random.choice(temp_list_cards)
                self.cards.append(find_item)
                temp_list_cards.remove(find_item)

        self.last_card = self.cards[len(self.cards) - 1]
        self.trump_suit = self.last_card.suit

        # установка признака козырной карты
        filter_trump = filter(lambda cart_trump: cart_trump.suit == self.trump_suit, self.cards)
        for cart_item in filter_trump:
            cart_item.is_trump = True

    def have_cards(self):
        return len(self.cards) != 0

    def give(self):
        current_cart = self.cards[0]
        self.cards.remove(current_cart)
        return current_cart

    def deck_cards_view(self):
        result = '?'
        if len(self.cards) <=5:
            result = str(len(self.cards))

        return self.last_card.name + ' осталось '+result+' карт'
class Card:
    "Класс для представления карты"

    # name = ""  # имя карты
    # priority = 0  # приоритет
    # suit = ""  # масть
    # number = 0
    # high = False  # карта выше 10

    def __init__(self, name, priority, suit, number, high):
        self.name = name
        self.priority = priority
        self.suit = suit
        self.number = number
        self.high = high
        self.is_trump = False
