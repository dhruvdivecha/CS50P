import random

while True:
    try:
        level = int(input("Level: "))

        if level > 0:
            break

    except:
        pass


ran_num = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))

        if guess > 0:
            if ran_num == guess:
                print("Just right!")
                break

            elif guess > ran_num :
                print("Too large!")

            elif guess < ran_num:
                print("Too small!")
    except:
        pass







