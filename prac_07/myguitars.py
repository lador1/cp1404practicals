"""
Time started 2.45pm
Time finsihed UNFINISHED
"""

from prac_06.guitar import Guitar

FILENAME = 'guitars.csv'


def main():
    guitars = load_guitars(FILENAME)
    print_guitars(guitars)


def load_guitars(FILENAME):
    guitars = []
    with open(FILENAME, "r") as in_file:
        for line in in_file:
            guitars.sort()
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], parts[1], parts[2])
            guitars.append(guitar)
    return guitars


def print_guitars(guitars):
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar.name:24} ({guitar.year}), worth ${guitar.cost}")

# def load_data(filename):
#
#
# def print_guitars(guitars):
#     print("These are my guitars:")
#     for i, guitar in enumerate(guitars, 1):
#         vintage_string = ""
#         if guitar.is_vintage():
#             vintage_string = " (vintage)"
#         print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
#

main()





# name = input("Name: ")
#     # while name != "":
#     #     year = int(input("Year: "))
#     #     cost = float(input("Cost: "))
#     #     print(f"{name} ({year}) : ${cost:.2f} added!")
#     #     new_guitar = Guitar(name, year, cost)  # Needed to make new guitar because append is only for 2 things
#     #     guitars.append(new_guitar)
#     #     name = input("Name: ")
#     #     print("\n... snip ...\n")
#     #     print_guitars(guitars)
#