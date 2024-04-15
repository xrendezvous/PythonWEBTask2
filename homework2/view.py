from abc import ABC, abstractmethod


class View(ABC):
    @abstractmethod
    def display_contacts(self, contacts):
        pass

    @abstractmethod
    def display_message(self, message):
        pass

    @abstractmethod
    def display_command_list(self, commands):
        pass


class ConsoleView(View):
    def display_contacts(self, contacts):
        for contact in contacts:
            print("_" * 50)
            print(f"Name: {contact['name']}\nPhones: {', '.join(contact['phones'])}\nBirthday: {contact['birthday']}\nEmail: {contact['email']}\nStatus: {contact['status']}\nNote: {contact['note']}")
            print("_" * 50)

    def display_message(self, message):
        print(message)

    def display_command_list(self, commands):
        format_str = str('{:%s%d}' % ('^', 20))
        for command in commands:
            print(format_str.format(command))
