"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    print_nicely(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []  # OPENS NEW LIST
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        data.append(parts)  # APPENDS PARTS (WHICH IS ALREADY A LIST) INTO A NEW LIST TO MAKE A NESTED LIST
        print("----------")
    input_file.close()
    return data


def print_nicely(data):
    for datum in data:
        print(f'{datum[0]} is taught by {datum[1]} and has {datum[2]} students')
        # print("{} is taught by {} and has {} students".format(*datum))


main()
