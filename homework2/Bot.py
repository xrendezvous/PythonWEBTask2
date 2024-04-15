from AddressBook import *
from view import ConsoleView


class Bot:
    def __init__(self, view):
        self.book = AddressBook()
        self.view = view

    def handle(self, action):
        if action == 'view':
            contacts = [contact for contact in self.book]
            self.view.display_contacts(contacts)
        elif action == 'help':
            commands = ['add', 'search', 'edit', 'load', 'remove', 'save', 'congratulate', 'view', 'exit']
            self.view.display_command_list(commands)
        else:
            if action == 'add':
                name = Name(input("Name: ")).value.strip()
                phones = Phone().value
                birth = Birthday().value
                email = Email().value.strip()
                status = Status().value.strip()
                note = Note(input("Note: ")).value
                record = Record(name, phones, birth, email, status, note)
                return self.book.add(record)
            elif action == 'search':
                print("There are following categories: \nName \nPhones \nBirthday \nEmail \nStatus \nNote")
                category = input('Search category: ')
                pattern = input('Search pattern: ')
                result = (self.book.search(pattern, category))
                for account in result:
                    if account['birthday']:
                        birth = account['birthday'].strftime("%d/%m/%Y")
                        result = ("_" * 50 + "\n" + f"Name: {account['name']} \nPhones: {', '.join(account['phones'])}" f" \nBirthday: {birth} \nEmail: {account['email']}" f" \nStatus: {account['status']}" f" \nNote: {account['note']}\n" + "_" * 50)
                        print(result)
            elif action == 'edit':
                contact_name = input('Contact name: ')
                parameter = input('Which parameter to edit(name, phones, birthday, status, email, note): ').strip()
                new_value = input("New Value: ")
                return self.book.edit(contact_name, parameter, new_value)
            elif action == 'remove':
                pattern = input("Remove (contact name or phone): ")
                return self.book.remove(pattern)
            elif action == 'save':
                file_name = input("File name: ")
                return self.book.save(file_name)
            elif action == 'load':
                file_name = input("File name: ")
                return self.book.load(file_name)
            elif action == 'congratulate':
                print(self.book.congratulate())
            elif action == 'view':
                print(self.book)
            elif action == 'exit':
                pass
            else:
                print("There is no such command!")
