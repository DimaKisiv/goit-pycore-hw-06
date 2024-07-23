from phone import Phone
from name import Name

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    def remove_phone(self, phone_str):
        phone = self.find_phone(phone_str)
        if phone:
            self.phones.remove(phone)
    def edit_phone(self, old_phone_str, new_phone_str):
        phone = self.find_phone(old_phone_str)
        if phone:
            phone.update_value(new_phone_str)
    def find_phone(self, phone_str):
        return next(iter([p for p in self.phones if p.value == phone_str]), None)
    
    