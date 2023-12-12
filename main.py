import json


phonebook = { }

def save() -> None:

    with open("phoneNumber.json", "w", encoding="utf-8") as doc:
        doc.write(json.dumps(phonebook, ensure_ascii=False))
    print("")


def load() -> dict:
    
    with open("phoneNumber.json", "r", encoding="utf-8") as doc:
        telephone = json.load(doc)
    print("")
    return telephone

def display_all() -> None:
   
    for name, info in phonebook.items():
        tel = ', '.join(map(str, info['phones'])) if 'phones' in info else ''
        br = info['birthday'] if 'birthday' in info else ''
        em = info['email'] if 'email' in info else ''
        print(f"{name}: tel - {tel}, birthday - {br}, email - {em}")
        print("-" * 20)  # Разделитель между контактами

def add_contact(
    name: str,
    phone: list,
    birthday: str,
    email: str
) -> None:
    
    phonebook[name] = {}  # Создаем новый словарь для контакта с именем 'name'

    if phone:  # Проверяем, что список телефонов не пустой
        phonebook[name]['phones'] = phone
    if birthday:  # Проверяем, что день рождения не пустая
        phonebook[name]['birthday'] = birthday
    if email:  # Проверяем, что email не пустой
        phonebook[name]['email'] = email

    print(f"Контакт {name} добавлен.\n")

def find_contact(
    name: str
) -> None:
   
    if name in phonebook:
        print(f"{name}: tel - {', '.join(map(str, phonebook[name]['phones']))}, birthday - {phonebook[name]['birthday']}, email - {phonebook[name]['email']}\n")
    else:
        print(f"Контакт {name} не найден.\n")

def change_contact(
    name: str
) -> None:
    
    if name in phonebook:
        while True:
            info = input(
                "Введите что вы хотите изменить: name, tel, birthday, email, save: ").lower(
                    ).replace(
                        " ", ""
                    )
            if info == "name":
                new_name = input("Введите имя: ")
                phonebook[new_name] = phonebook.pop(name)  # Удаляем старый ключ и получаем его значение
            elif info == "tel":
                phone = list(map(int, input("Введите номера телефонов через пробел: ").split()))
                phonebook[name]['phones'] = phone
            elif info == "birthday":
                birthday = input("Введите дату рождения: ")
                phonebook[name]['birthday'] = birthday
            elif info == "email":
                email = input("Введите EMAIL: ")
                phonebook[name]['email'] = email
            elif info == "save":
                break
            else:
                print("Вы ввели не верную комманду, изучите мануал!")
        print(f"Контакт {name} изменен.\n")
    else:
        print(f"Контакт {name} не найден.")

def delete_contact(
    name: str
) -> None:
   
    if name in phonebook:
        del phonebook[name]
        print(f"Контакт {name} удален.\n")
    else:
        print(f"Контакт {name} не найден.\n")

try:
    phonebook = load()
except:
    phonebook = { }

while True:
    command = input("Введите команду /load /save /all /add /change /delete /find /exit: ")

    if command == "/load":
        print("Данные загружены\n")
        phonebook = load()
    elif command == "/save":
        save()
        print("Новая запись добавлена")
    elif command == "/all":
        print("Текущий телефонный список")
        print(display_all())
    elif command == "/add":
        name = input("Введите имя: ")
        phone = list(map(int, input("Введите номера телефонов через пробел: ").split()))
        birthday = input("Введите дату рождения: ")
        email = input("Введите EMAIL: ")

        add_contact(
            name=name,
            phone=phone,
            birthday=birthday,
            email=email,
        )
    elif command == "/find":
        name = input("Введите имя: ")
        find_contact(
            name=name,
        )
    elif command == "/change":
        name = input("Введите имя: ")
        change_contact(
            name=name,
        )
    elif command == "/delete":
        name = input("Введите имя: ")
        delete_contact(
            name=name,
        )
    elif command == "/exit":
        print("До встречи!")
        break
    else:
        print("Вы ввели не верную комманду, изучите мануал!\n")
