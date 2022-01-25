import random

user_wins = 0
comp_wins = 0

options = ['rock', 'paper', 'scissors']


while True:
    pick = input("Type Rock/Paper/Scissors or type Q to quit: ")

    if pick.lower() == 'q':
        break

    if pick.lower() not in options:
        continue

    rand = random.randint(0, 2)

    if rand == 0:
        print("User : {} Computer : Rock" .format(pick))
        if pick.lower() == 'paper':
            print("You won! :)")
            user_wins += 1
        elif pick.lower() == 'rock':
            print("No winner :\ ")
            continue
        else:
            print("You lost!  :(")
            comp_wins += 1

    if rand == 1:
        print("User: {} Computer : Paper" .format(pick))
        if pick.lower() == 'scissors':
            print("You won! :)")
            user_wins += 1
        elif pick.lower() == 'paper':
            print("No winner :\ ")
            continue
        else:
            print("You lost! :(")
            comp_wins += 1

    if rand == 2:
        print("User: {} Computer : Scissors" .format(pick))
        if pick.lower() == 'rock':
            print("You won! :)")
            user_wins += 1
        elif pick.lower() == 'scissors':
            print("No winner :\ ")
            continue
        else: 
            print("You lost! :(")
            comp_wins +=1

if user_wins > comp_wins:
    print("You won {} time(s) :) \nComputer won {} time(s)" .format(user_wins, comp_wins))

else:
    print("You won {} time(s) :( \nComputer won {} time(s)" .format(user_wins, comp_wins))

        
