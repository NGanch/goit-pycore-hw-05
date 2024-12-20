# Декоратор для обробки помилок
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Give me a command."
    return inner

# Словник для зберігання контактів
contacts = {}

# Функція для додавання контакту
@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError  # Якщо не два аргументи, викликається ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# Функція для пошуку телефону за ім'ям
@input_error
def get_phone(args, contacts):
    if len(args) == 0:
        raise IndexError  # Якщо не передано жодного аргументу
    name = args[0]
    return contacts[name]

# Функція для виведення всіх контактів
@input_error
def show_all_contacts(args, contacts):
    if len(contacts) == 0:
        raise IndexError  # Якщо немає контактів
    return '\n'.join([f"{name}: {phone}" for name, phone in contacts.items()])

# Основна функція бота
def start_bot():
    while True:
        command = input("Enter a command: ").strip().lower()
        
        if command == "add":
            args = input("Enter the argument for the command (name and phone): ").split()
            print(add_contact(args, contacts))
        elif command == "phone":
            args = input("Enter the argument for the command (name): ").split()
            print(get_phone(args, contacts))
        elif command == "all":
            print(show_all_contacts([], contacts))  # Не потрібно передавати аргументи
        elif command == "exit":
            print("Goodbye!")
            break
        else:
            print("Unknown command. Please try again.")

# Запуск бота
start_bot()