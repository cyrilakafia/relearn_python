import time
status = ""
users = {}

def mainMenu():
    global status
    status = input("Do you have a login accounnt? y/n? Or press q to quit: ")
    if status == "y" or status == "Y":
        oldUser()
    elif status == "n" or status == "N":
        newUser()
    elif status == "q" or status == "Q":
        quit()

def newUser():
    createLogin = input("Creat a login name: ")

    if createLogin in users:
        print("\nLogin name already exists!\n")
    else:
        createPassw = input("Create password: ")
        users[createLogin] = createPassw
        print("\nUser created!\n")
        logins = open("C:\\Users\\Cyril\\Documents\\logins.txt", "a")
        logins.write(createLogin + " " + createPassw + "\n")
        logins.close()

def oldUser():
    login = input("Enter login name: ")
    passw = input("Enter password: ")

    filx = open("C:\\Users\\Cyril\\Documents\\logins.txt")
    userx = filx.readlines()
    # check if user exists and login matches password

    if login in users and users[login] == passw:
        print("\nLogin successful!\n")
        print("User:", login, "accessed the system on:", time.asctime())
    else:
        for i in userx:
            checkerx = "n"
            if login in i and passw in i:
                print("\nLogin successful!\n")
                print("User:", login, "accessed the system on:", time.asctime())
                checkerx = "y"
                break
        if checkerx == "n":
            print("\nInvalid username or password\n")

while status != "q":
    mainMenu()