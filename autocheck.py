class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def info(self):
        return {'name': self.name, 'age': self.age, 'address': self.address}

class Dog(Animal):
    def __init__(self, nickname, weight, breed, owner):
        super().__init__(nickname, weight)
        self.breed = breed
        self.owner = owner

    def say(self):
        return "Woof"

    def who_is_owner(self):
        return self.owner.info()

owner_info = {'name': 'John', 'age': 35, 'address': '123 Main St'}
owner = Owner(**owner_info)

dog = Dog("Barbos", 23, "labrador", owner)

print("Ім'я собаки:", dog.nickname)
print("Вага собаки:", dog.weight)
print("Порода собаки:", dog.breed)
print("Звук, який видає собака:", dog.say())

print("Інформація про власника собаки:", dog.who_is_owner())
