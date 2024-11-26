def main():
    greet = input("Greet me: ")
    greet = value(greet)
    print(f"${greet}")


def value(greeting):
    greeting = greeting.lower()
    greeting = greeting.strip()

    if 'hello' in greeting:
        return 0
    elif 'h' in greeting[0]:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
