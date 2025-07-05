
from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_full_info(self):
        pass


class Person(User):

    def __init__(self, name, age):
        super().__init__(name, age)

    #def get_full_info(self):
    #    return f'Name = {self.name} age = {self.age}'


class Bot(User):
    def __init__(self, name):
        super().__init__(name, 10)

    def get_full_info(self):
        return f'Bot {self.name}'


person = Person('Иван', 10)
user = User('Петр', 10)
bot = Bot('Бот')

#print(person.get_full_info())
print(user.get_full_info())
print(bot.get_full_info())
