FILENAME = "wimbledon.csv"


def main():
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            new = line.split(',')
            print(new)


main()
