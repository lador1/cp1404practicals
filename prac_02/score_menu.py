"""
Score Menu
Luca Adornetto
"""
MENU = """S - Enter score between 0-100
R - Print Result
* - Print score in stars
Q - Quit"""


def main():
    print(MENU)
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "S":
            score = get_score()
        elif choice == "R":
            print(score)
        elif choice == "S":
            stars = print_stars()
        else:
            print("Invalid choice")
        print("Menu: ")
        choice = input("> ").upper()
    print("farewell")


def get_score(score):
    score = input("Score: ")
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
    return message


def print_stars(score):
    for i in range(score):
        print('*', end=' ')


main()