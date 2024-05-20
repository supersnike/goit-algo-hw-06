from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Ім'я не може бути порожнім")
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if not self.validate_phone(value):
            raise ValueError("Номер телефону повинен містити 10 цифр")
        super().__init__(value)

    @staticmethod
    def validate_phone(value):
        return value.isdigit() and len(value) == 10


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        phone_to_remove = None
        for phone in self.phones:
            if phone.value == phone_number:
                phone_to_remove = phone
                break
        if phone_to_remove:
            self.phones.remove(phone_to_remove)

    def edit_phone(self, old_phone_number, new_phone_number):
        for phone in self.phones:
            if phone.value == old_phone_number:
                phone.value = new_phone_number
                return
        raise ValueError("Номер телефону не знайдено")

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self):
        phones_str = ', '.join(phone.value for phone in self.phones)
        return f"Ім'я контакту: {self.name.value}, телефони: {phones_str}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError("Контакт не знайдено")


# Тестування реалізації

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у адресній книзі
print("Всі контакти в адресній книзі:")
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print("\nКонтакт John після редагування телефону:")
print(john)  # Виведення: Ім'я контакту: John, телефони: 1112223333, 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"\nЗнайдено номер телефону для контакту {john.name.value}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")

# Перевірка видалення Jane
try:
    jane = book.find("Jane")
    if jane is None:
        print("\nJane не знайдено в адресній книзі")
    else:
        print(jane)
except KeyError:
    print("\nJane не знайдено в адресній книзі")
