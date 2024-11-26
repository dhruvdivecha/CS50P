def main():
    msg = input()
    result = convert(msg)
    print(result)

def convert(msg):
    msg0 = msg.replace(":)", "🙂")
    msg1 = msg0.replace(":(", "🙁")
    return msg1

main()
