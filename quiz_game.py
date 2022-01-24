def beginx():
    print("Welcome to Beginner Mode")
    scorex = 0
    ques_1 = input("What is the full meaning of CPU? ")
    if ques_1.lower() == 'central processing unit':
        scorex += 1

    ques_2 = input("What is the full meaning of RAM? ")
    if ques_2.lower() == 'random acess memory':
        scorex += 1

    ques_3 = input("What is the full meaning of ROM? ")
    if ques_3.lower() == 'read only memory':
        scorex += 1
    
    if scorex <= 1:
        print("You scored {}/3 :(" .format(scorex))
    else:    
        print("You scored {}/3 :)" .format(scorex))

def amateurx():
    print("Welcome to Amateur Mode")
    scorex = 0
    ques_1 = input("What is the full meaning of PSU? ")
    if ques_1.lower() == 'power supply unit':
        scorex += 1

    ques_2 = input("What is the full meaning of ICT? ")
    if ques_2.lower() == 'information communication technology':
        scorex += 1

    ques_3 = input("What is the full meaning of HTML? ")
    if ques_3.lower() == 'hypertext transfer markup language':
        scorex += 1
    
    if scorex <= 1:
        print("You scored {}/3 :(" .format(scorex))
    else:    
        print("You scored {}/3 :)" .format(scorex))

def profx():
    print("Welcome to Professional Mode")
    scorex = 0
    ques_1 = input("What measurment system is used in the USA? ")
    if ques_1.lower() == 'imperial system' or ques_1.lower() == 'imperial' or ques_1.lower() == 'imperial measurment system':
        scorex += 1

    ques_2 = input("What is the full meaning of RAM? ")
    if ques_2.lower() == 'random acess memory':
        scorex += 1

    ques_3 = input("What is the full meaning of ROM? ")
    if ques_3.lower() == 'read only memory':
        scorex += 1
    
    if scorex <= 1:
        print("You scored {}/3 :(" .format(scorex))
    else:    
        print("You scored {}/3 :)" .format(scorex))

print("Welcome To The Quiz Game! :)")
quesx = input("Do you want to play. Yes or No? ")

if quesx.lower() == 'yes':
    print("Enter Difficulty: Beginner Amateur Professional\n")
    diffx = input()
    if diffx.lower() == 'beginner':
        beginx() 
    
    elif diffx.lower() == 'amateur':
        amateurx()
    
    elif diffx.lower() == 'professional':
        profx()

else:
    quit()

