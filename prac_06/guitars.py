"""
Start: 9.48
Finish:


"""

from prac_06.guitar import Guitar

"""Create a program that inputs guitars and sorts to a list"""


def main():
    # print("My Guitars:")
    guitars = []
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        print(f"{name} ({year}) : ${cost:.2f} added!")
        new_guitar = Guitar(name, year, cost)  # Needed to make new guitar because append is only for 2 things
        guitars.append(new_guitar)
        name = input("Name: ")
        print("\n... snip ...\n")

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = " (vintage)"
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
