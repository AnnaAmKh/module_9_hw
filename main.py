
contacts = {}  # словник для зберігання контактів


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid command. Try again."

    return wrapper


@input_error
def add_contact(command):
    _, name, phone = command.split()
    contacts[name] = phone
    return f"Contact {name} with phone number {phone} added"


@input_error
def change_phone(command):
    _, name, phone = command.split()
    contacts[name] = phone
    return f"Phone number for contact {name} changed to {phone}"


@input_error
def show_phone(command):
    _, name = command.split()
    return contacts[name]


@input_error
def show_all_contacts(command):
    if not contacts:
        return "No contacts found."
    else:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    while True:
        user_input = input("Enter command: ").lower()

        if user_input == "hello":
            print("How can I help you?")

        elif user_input.startswith("add"):
            print(add_contact(user_input))

        elif user_input.startswith("change"):
            print(change_phone(user_input))

        elif user_input.startswith("phone"):
            try:
                print(show_phone(user_input))
            except KeyError:
                print("Contact not found.")

        elif user_input == "show all":
            print(show_all_contacts(user_input))

        elif user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break

        else:
            print("Invalid command. Try again.")


if __name__ == "__main__":
    main()
