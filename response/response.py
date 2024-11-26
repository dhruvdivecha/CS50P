from validator_collection import checkers


def main():
    print(validate(input("Text: ")))

def validate(email):
    if checkers.is_email(email):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()

