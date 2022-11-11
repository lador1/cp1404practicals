"""
Score Menu
Luca Adornetto
"""
MENU = """D - Display Movies
A - Add new movie
W - Watch a movie
Q - Quit"""


def main():
    print(MENU)
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "S":
            score = get_score()
        elif choice == "R":
            print(score)
        elif choice == "*":
            print_stars(score)
        else:
            print("Invalid choice")
        print("Menu: ")
        choice = input("> ").upper()
    print("farewell")


def get_score():
    score = int(input("Score: "))
    if score > 100:
        message = 'Invalid score'
    elif score >= 90:
        message = "Excellent"
    elif score >= 50:
        message = "Passable"
    elif score < 50:
        message = "Bad"
    else:
        message = "Invalid score"
    print(message)
    return score


def print_stars(score):
    for i in range(score):
        print('*', end=' ')


main()
