"""
CP1404/CP5632 - Practical
Luca Adornetto
"""


def main():
    score = float(input("Enter score: "))


def determine_score_message(score):
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


def print_message(message):
    print(f"{message}")


main()
