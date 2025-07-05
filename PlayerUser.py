from Player import Player
class PlayerUser(Player):
    def cart_view(self):
        result = ''
        index = 1
        for cart_item in self.cards:
            result += ' [' + str(index) + '] ' + cart_item.name + ' | '
            index += 1

        result += ' [0]  Пас'
        return result