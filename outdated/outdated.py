months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()
    try:
        month, day, year = date.split("/")
        month = int(month)
        day = int(day)
        year = int(year)
        if 0 < month < 13 and 0 < day < 32:
            if year >= 1000 and year <= 9999:
                print(f"{year}-{month:02}-{day:02}")
                break
    except:
        try:
            if "," in date:
                month, day, year = date.split(" ")
                day = day.replace(',', "")
                day = int(day)
                year = int(year)
                month = month.capitalize()
                if month in months and (0 < day < 32):
                    if 1000 <= year <= 9999:
                        month = months.index(month)+1
                        print(f"{year}-{month:02}-{day:02}")
                        break
        except:
            pass
