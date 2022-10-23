FILENAME = "wimbledon.csv"
INDEX_OF_COUNTRY = 1
INDEX_OF_CHAMPION = 2


def main():
    records = get_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def process_records(records):
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_OF_COUNTRY]) #Add index one to dictionary
        try:
            champion_to_count[record[INDEX_OF_CHAMPION]] += 1 #Add index two to dictionary (champ)
        except KeyError:
            champion_to_count[record[INDEX_OF_CHAMPION]] = 1
    return champion_to_count, countries


def display_results(champion_to_count, countries):
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


def get_records(filename):
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()