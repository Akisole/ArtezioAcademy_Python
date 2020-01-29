# Написать программу, которая принимает от пользователя имя и пароль.
# Сравнивает пароль с заданным в коде.


def sign_in():
    while True:
        print("Your login:")
        name = input()
        print("Password:")
        password = input()

        if name in DB:
            if DB.get(name) == password:
                print("Wellcome,", name)
                break
        print("Login or password is incorrect")
        print("Please try again...\n")


DB = {'Sasha': 'qwerty', 'Olga': 'asdfgh', 'Nikita': 'zxcvbn'}
sign_in()
