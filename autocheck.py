class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return "Meow"


class CatDog:
    def __init__(self, nickname, weight):
        self.cat = Cat(nickname, weight)  # Створення екземпляру класу Cat

    def say(self):
        return self.cat.say()  # Делегування методу say до класу Cat

    def change_weight(self, weight):
        self.cat.change_weight(weight)  # Делегування методу change_weight до класу Cat


# Приклад використання
catdog = CatDog("Fluffy", 5)
print(catdog.say())  # Виведе: Meow
catdog.change_weight(6)
print(catdog.cat.weight)  # Виведе: 6