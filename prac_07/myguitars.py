"""
Time started 2.45pm
Time finsihed UNFINISHED
"""
import csv
from prac_06.guitar import Guitar
FILENAME = 'guitars.csv'


def main():
    guitars = load_guitars(FILENAME)
    print_guitars_list(guitars)


def load_guitars(FILENAME):
    guitars = []
    with open(FILENAME, "r") as in_file:
        for line in in_file:
            guitars.sort()
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], parts[1], parts[2])
            guitars.append(guitar)
    return guitars


def print_guitars_list(guitars):
    """Print the guitars in the csv file"""
    print("Guitars loaded from file")
    for i, guitar in enumerate(guitars, 1):
        print(f"{i}: {guitar.name:24} ({guitar.year}), worth ${guitar.cost}")
    update_guitars_list(guitars)


def update_guitars_list(guitars):
    """Allow user to enter guitar info and update to list"""
    name = input("Add a new guitar: ")
    if name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitar = Guitar(name, year, cost)  # Needed to make new guitar because append is only for 2 things
        guitars.append(new_guitar)
        print(f"\n {name} ({year}) : ${cost:.2f} added! \n")
        print_guitars_list(guitars)
    else:
        save_updated_guitar_list(FILENAME, guitars)


def save_updated_guitar_list(FILENAME, guitars):
    """save added guitars to csv file"""
    with open(FILENAME, "w", encoding="UTF-8") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file, end="\n")


main()
