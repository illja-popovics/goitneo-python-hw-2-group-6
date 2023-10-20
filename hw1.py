def input_error(func): #decorator to handle exceptions
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid input. Please provide the required information."
    return inner

@input_error # possible exceptions here, but not likely
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def show_all(contacts): # no need for exception handling
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

@input_error 
def phone_contact(args, contacts):
    if len(args) == 1:
        phone = args[0]
        if phone in contacts:
            print(contacts[phone])
        else:
            print("Contact not found.")
    else:
        print("Invalid input. Please provide a name.")

@input_error
def add_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    else:
        return "Invalid input. Please provide a name and a phone number."

@input_error
def change_contact(args, contacts):
    if len(args) == 2:
        name, new_phone = args
        if name in contacts:
            contacts[name] = new_phone
            return "Contact updated."
        else:
            return "Contact not found."
    else:
        return "Invalid input. Please provide a name and a new phone number."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            show_all(contacts)
        elif command == "help":
            print("Available commands: add, change, phone, all, help, close, exit")
        elif command == "phone":
            phone_contact(args, contacts)
        else:
            print("Invalid command.")



if __name__ == "__main__":
    main()