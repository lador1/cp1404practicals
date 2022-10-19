FILENAME = "wimbledon.csv"


def main():
    get_file()
    convert_records_to_dictionary()


def convert_records_to_dictionary(records):
    """Create dictionary of champions and set of countries from records (list of lists)."""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[1])
        try:
            champion_to_count[record[1]] += 1
        except KeyError:
            champion_to_count[record[2]] = 1
    return champion_to_count, countries


def display_results(records):
    champion_to_count = {records}


def get_file(filename):
    "Get records from file and display in list"
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            records.append(parts)
        return records


main()
