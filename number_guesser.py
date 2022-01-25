import random

while True:
    try:
        num = int(input("Enter a upper limit: "))
    except ValueError:
        print("Enter an Integer!")
    else:
        break

random_num = random.randint(0, num)
guess = 0

while True:
    guess += 1
    try:
        guess_num = int(input("Guess the random number: "))
        if guess_num == random_num:
            print("You got it right! :)")
            print("You got it right in {} tries!" .format(guess))
            break
        elif guess_num > random_num:
            print("You got it wrong. You were above the number")
        elif guess_num < random_num:
            print("You got it wrong. You were below the number")
    except ValueError:
        print("Enter an Integer!")

