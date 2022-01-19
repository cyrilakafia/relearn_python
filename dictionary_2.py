#this code accepts input into a dictionary
#this code accepts name and phone numbers to simulate a phone book

phonebook = dict()

while True:
    name = input("Enter your name or type 'done': ")
    if name == "done":
        break
    elif name in phonebook:
        print("Name already exists. Use a different name")
    else:
        while True:
            try:
                num = input("Enter your number: ")
                number = int(num)
                break
            except ValueError:
                print("Invalid Input! Enter an integer")

    phonebook[name] = number

print(phonebook)
