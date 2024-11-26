
def main():
     fraction = input("Fraction: ")
     fraction = convert(fraction)
     fuel = gauge(fraction)
     print(fuel)


def convert(fraction):
    while True:

        try:
            upper, lower = fraction.split("/")
            upper, lower = int(upper), int(lower)

            fraction = (upper/lower)

            if fraction <= 1:
                p = int(fraction * 100)
                return p
            else:
                fraction = input("Fraction: ")
                pass

        except(ValueError, ZeroDivisionError):
            pass


def gauge(percentage):

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()



