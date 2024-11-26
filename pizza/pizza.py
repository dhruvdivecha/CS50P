import sys
import tabulate
import csv

def main():
    check_argv()

    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            print(tabulate.tabulate(reader, headers = "keys", tablefmt = "grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")


def check_argv():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too mant command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
