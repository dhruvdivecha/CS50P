import sys
import csv

def main():
    check_argv()
    output = []

    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)

            for row in reader:
                split_name = row["name"].split(",")
                output.append({'first': split_name[1].lstrip(), 'last': split_name[0].lstrip(), 'house': row["house"]})

    except FileNotFoundError:
        sys.exit("File does not exist")

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house":"house"})
        for row in output:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})

def check_argv():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too mant command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
