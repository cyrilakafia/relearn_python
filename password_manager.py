from cryptography.fernet import Fernet

# def write_key():
#     key = Fernet.generate_key()
#     with open("C:\\Users\\Cyril\\Documents\\Code\\Python\\Python Code\\password_manager\\key.key", "wb") as key_file:
#         key_file.write(key)

def load_key():
    filex = open("C:\\Users\\Cyril\\Documents\\Code\\Python\\Python Code\\password_manager\\key.key", "rb")
    key = filex.read()
    filex.close()
    return key

key = load_key()
fer = Fernet(key)


def view_passw():
    fview = open("C:\\Users\\Cyril\\Documents\\Code\\Python\\Python Code\\password_manager\\password.txt")
    for f in fview.readlines():
        line = f.rstrip()
        username, password = line.split("|")
        print("Username: {} | Password: {}" .format(username, fer.decrypt(password.encode()).decode()))


def add_passw():
    usern = input("Enter your username: ")
    passw = input("Enter your password: ")

    fopen = open("C:\\Users\\Cyril\\Documents\\Code\\Python\\Python Code\\password_manager\\password.txt", 'a')
    fopen.write("{}|{}\n" .format(usern, fer.encrypt(passw.encode()).decode()))
    fopen.close()


while True:  
    ans = input("Type 'Add' if you want to add a new password or type 'View' if you want to view all passwords: ")

    if ans.lower() == 'q':
        quit()

    elif ans.lower() == 'add':
        add_passw()

    elif ans.lower() == 'view':
        view_passw()

    else:
        print("Invalid input")
        continue