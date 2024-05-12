from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        value_str = str(value)  # Перетворення значення на рядок
        if len(value_str) != 10:
            raise ValueError("Телефон повинен містити рівно 10 цифр")
        super().__init__(value_str)



class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def delete_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != phone]

    def edit_phone(self, old_phone, new_phone):
        for i, phone in enumerate(self.phones):
            if str(phone) == old_phone:
                self.phones[i] = Phone(new_phone)
                break

    def __str__(self):
        return f"Контакт: {self.name.value}, Телефон: {'; '.join(str(p) for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def delete_record(self, name):
        del self.data[name]

    def search_by_name(self, name):
        return self.data.get(name, None)

    def search_by_phone(self, phone):
        for record in self.data.values():
            for p in record.phones:
                if str(p) == phone:
                    return record
        return None

    def delete_contact(self, name):
        if name in self.data:
            del self.data[name]
            return f"Запис '{name}' видалено."
        else:
            return f"Запис '{name}' не знайдено."

def parse_input(user_input):
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args

def input_error(func):
    """Декоратор для обробки помилок вводу."""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Контакт не знайдено."
        except IndexError:
            return "Не вірна команда."
        except ValueError as ve:
            if str(ve) == "Телефон повинен містити рівно 10 цифр":
                return "Телефонний номер повинен містити рівно 10 цифр."
            else:
                return "Не вірний ввод. Додайте данні."
        except Exception as e:
            return f"Помилка: {e}"
    return inner

@input_error
def add_contact(args, address_book):
    name, phone = args
    if not name or not phone:
        raise ValueError
    if name in address_book.data:
        return f"Контакт '{name}' вже присутній."
    record = Record(name)
    record.add_phone(phone)
    address_book.add_record(record)
    return f"Контакт '{name}' додано."

@input_error
def change_contact_phone(args, address_book):
    if len(args) != 2:
        raise IndexError
    name, phone = args
    record = address_book.search_by_name(name)
    if record:
        record.edit_phone(record.phones[0].value, phone)
        return f"Номер телефону контакту '{name}' змінено."
    else:
        raise KeyError

@input_error
def display_contact_phone(args, address_book):
    if len(args) != 1:
        raise IndexError
    name = args[0]
    record = address_book.search_by_name(name)
    if record:
        return f"Телефонний номер контакту '{name}': {record.phones[0].value}"
    else:
        raise KeyError

def display_all_contacts(address_book):
    if address_book.data:
        print("Всі контакти:")
        for name, record in address_book.data.items():
            print(record)
    else:
        print("Не знайдено жодного контакту.")

def main():
    address_book = AddressBook()
    print("Вас вітає бот асистент!")
    while True:
        user_input = input("Введіть команду: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Хай щастить!")
            break
        elif command == "hello":
            print("Чим я можу допомогти?")
        elif command == "add":
            print(add_contact(args, address_book))
        elif command == "change":
            print(change_contact_phone(args, address_book))
        elif command == "phone":
            print(display_contact_phone(args, address_book))
        elif command == "all":
            display_all_contacts(address_book)
        elif command == "delete":
            print( address_book.delete_contact(args[0]))
        else:
            print("Не вірна команда.")

if __name__ == "__main__":
    main()
