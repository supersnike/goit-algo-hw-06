class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, new_weight):
        self.weight = new_weight


animal = Animal("Simon", 10)
print("Кличка тварини:", animal.nickname)  # Очікуємо "Simon"
animal.change_weight(12)
print("Оновлена вага:", animal.weight)