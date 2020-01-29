# Написать программу, которая принимает от пользователя имя и пароль.
# Сравнивает пароль с заданным в коде.


def sign_in():
    checkingpassword = 'qwerty'

    print("Your login:")
    name = input()
    print("Password:")
    while True:
        password = input()
        if password == checkingpassword:
            print("Password for user:", name, "is correct")
            break
        print("Password for user:", name, "is incorrect")
        print("Please try again...")


sign_in()
