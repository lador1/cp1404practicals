import csv  # Importing module first

from prac_06.city import City

FILENAME = "countries.csv"

"""
load a CSV file using the csv module, format data and create a list (CSV row) then create a City class to use as the values in a dictionary.
"""


# csv reader gives us already split line eliminating parts
def main():
    """Countries from csv program"""
    country_to_capital = load_data(FILENAME)
    print("Welcome, what do you want?: ")
    while True:
        country = input("Country: ")
        try:
            print(country_to_capital[country])
            break
        except KeyError:
            print("Country is not in the list")


def load_data(filename):
    """Load csv data as dictionary of Country: City object"""
    country_to_capital = {}
    with open(filename, "r") as in_file:
        in_file.readline()  # Ignore CSV header line
        reader = csv.reader(in_file)
        for row in reader:
            row[2] = int(row[2].replace(",", ""))  # Replace commas with nothing to remove 'string' make INT
            row[3] = float(row[3][:-1])  # Slicing to remove the last value (the %)
            row[4] = int(row[4])  # Remove '' from the year to make INT
            city = City(row[1], row[2], row[3])
            print(city)
            country_to_capital[row[0]] = city  # Country to city, row 0 = country, city has the city class
    return country_to_capital


main()
