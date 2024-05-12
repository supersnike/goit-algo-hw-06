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
        if not isinstance(value, str) or len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must be a string of 10 digits")
        super().__init__(value)

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
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def delete_record(self, name):
        del self.data[name]

    def search_by_name(self, name):
        return self.data.get(name, None)

    def search_by_phone(self, phone):
        for record in self.data.values():
            if phone in [str(p) for p in record.phones]:
                return record
        return None

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
            return "Contact not found."
        except IndexError:
            return "Invalid command. Usage: command args"
        except ValueError:
            return "Invalid input. Please enter valid arguments."
        except Exception as e:
            return f"An error occurred: {e}"
    return inner

@input_error
def add_contact(args, address_book):
    name, phone = args
    if not name or not phone:
        raise ValueError
    if name in address_book.data:
        return f"Contact '{name}' already exists."
    record = Record(name)
    record.add_phone(phone)
    address_book.add_record(record)
    return "Contact added."

@input_error
def change_contact_phone(args, address_book):
    if len(args) != 2:
        raise IndexError
    name, phone = args
    record = address_book.search_by_name(name)
    if record:
        record.edit_phone(record.phones[0].value, phone)
        return f"Phone number for contact '{name}' changed."
    else:
        raise KeyError

@input_error
def display_contact_phone(args, address_book):
    if len(args) != 1:
        raise IndexError
    name = args[0]
    record = address_book.search_by_name(name)
    if record:
        return f"Phone number for contact '{name}': {record.phones[0].value}"
    else:
        raise KeyError

def display_all_contacts(address_book):
    if address_book.data:
        print("All contacts:")
        for name, record in address_book.data.items():
            print(record)
    else:
        print("No contacts found.")

def main():
    address_book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, address_book))
        elif command == "change":
            print(change_contact_phone(args, address_book))
        elif command == "phone":
            print(display_contact_phone(args, address_book))
        elif command == "all":
            display_all_contacts(address_book)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
