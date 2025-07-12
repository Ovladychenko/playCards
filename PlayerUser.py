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

    def make_move(self):
        print('Ход пользователя')