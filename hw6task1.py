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
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must contain 10 digits")
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

    def find_phone(self, phone):
        for p in self.phones:
            if str(p) == phone:
                return p.value

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def delete_record(self, name):
        del self.data[name]

    def find(self, name):
        return self.data.get(name)

    def search_name(self, name):
        result = []
        for record in self.data.values():
            if record.name.value.lower() == name.lower():
                result.append(record)
        return result

    def search_phone(self, phone):
        result = []
        for record in self.data.values():
            if phone in [str(p) for p in record.phones]:
                result.append(record)
        return result
