contacts = {}

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid input. Format: command name phone"
    return wrapper

@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return f"Added {name} with phone number {phone}"

@input_error
def change_phone(name, phone):
    if name in contacts:
        contacts[name] = phone
        return f"Changed phone number for {name} to {phone}"
    else:
        return f"Contact {name} not found"

@input_error
def get_phone(name):
    if name in contacts:
        return f"The phone number for {name} is {contacts[name]}"
    else:
        return f"Contact {name} not found"

def show_all_contacts():
    if contacts:
        result = "Contacts:\n"
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result.strip()
    else:
        return "No contacts found"

def main():
    print("How can I help you?")
    while True:
        command = input().strip().lower()
        if command == "good bye" or command == "close" or command == "exit":
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command.startswith("add"):
            try:
                _, name, phone = command.split()
                print(add_contact(name, phone))
            except ValueError:
                print("Invalid input. Format: add name phone")
        elif command.startswith("change"):
            try:
                _, name, phone = command.split()
                print(change_phone(name, phone))
            except ValueError:
                print("Invalid input. Format: change name phone")
        elif command.startswith("phone"):
            try:
                _, name = command.split()
                print(get_phone(name))
            except ValueError:
                print("Invalid input. Format: phone name")
        elif command == "show all":
            print(show_all_contacts())
        else:
            print("Invalid command. Type 'hello' for instructions.")

if __name__ == "__main__":
    main()
