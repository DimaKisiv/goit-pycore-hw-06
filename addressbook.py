from collections import UserDict
from record import Record

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    def find(self, name) -> Record:
        record = self.data.get(name)
        return record
    def delete(self, name):
         self.data.pop(name)