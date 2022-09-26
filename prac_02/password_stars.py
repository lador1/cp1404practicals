"""
CP1404- Practical 2
Luca Adornetto
Password checker
"""
MIN_LENGTH = 5


def main():
    i = 0
    while i != 1:
        password = input('Enter a password: ')
        if len(password) < MIN_LENGTH:
            print('Password needs to be longer')
        else:
            i = 1
            print_password(password)


def print_password(password):
    for i in range(0, len(password)):
        print('*', end=' ')


main()
