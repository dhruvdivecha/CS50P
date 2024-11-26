# This project takes the student number and their first names and makes a custom email that can be used in their school.

import sys
import csv

def main():
    check_args()
    data = []
    try:
        with open(sys.argv[1]) as csvfile:
            reader = csv.DictReader(csvfile)
            for info in reader:
                data.append(info)

    except FileNotFoundError:
        sys.exit("Incorrect csv")

    output = []
    for row in data:
        email = make_email(row["name"], row["sn"])
        year_joined = year(row["sn"])
        output.append({"name": row["name"],"email": email, "year_joined": year_joined})

    with open(sys.argv[2], 'w') as file:
        writer = csv.DictWriter(file, fieldnames=["name","email","year_joined"])
        writer.writerow({"name": "name", "email": "email", "year_joined": "year_joined"})
        for row in output:
            writer.writerow({"name": row["name"], "email": row["email"], "year_joined": row["year_joined"]})

def check_args():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1] and ".csv" not in sys.argv[2]:
        sys.exit("Not a csv file")


def make_email(name, sn):
    email = sn + name + "@harvard.edu"
    return email.lower()

# the year joined are the first two numbers in the sn
def year(sn):
    first_two_digits = sn[1:3]
    year = "20" + first_two_digits
    return year


if __name__ == "__main__":
    main()
