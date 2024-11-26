from datetime import date
import sys
import re
import inflect
p = inflect.engine()

def main():
    birthday = input("Date of Birth: ")
    year, month, day = Validity(birthday)
    birthday = date(year, month, day)
    today_date = date.today()
    subtraction = today_date - birthday
    minutes = subtraction.days * 24 * 60
    print(p.number_to_words(minutes, andword = '').capitalize(),"minutes")


def Validity(birthday):
    try:
        if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birthday):
            year, month, day = birthday.split("-")
        return int(year), int(month), int(day)

    except:
        sys.exit("Inavlid Date")


if __name__ == "__main__":
    main()
