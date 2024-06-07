#the requirements for password:
#   1. at least 8 characters
#   2. at least one lower case character
#   3. at least one upper case character
#   4. at least one number
#   5. at least one special character($ or _ or @)
#
# the requirements for email:
#   an email with characters, numbers and a dot(.)
#
#The info will be saved in  a file named "save.txt"


import re           #this module is used to check the password and email validity
import password_generator as pg
from cryptography.fernet import Fernet
import inquirer


def update():                       #this function will open a new file "save.txt" and write the email and password
    with open("save.txt", "a") as a:
        a.write(f"Email: {email}\n")
        a.write(f"Password: {encrypted_password}\n________________\n\n")
    print("\nThe info has been saved!\nYou can view it in save.txt")

def encryption():

    key = Fernet.generate_key()
    fernet = Fernet(key)

    global encrypted_password
    encrypted_password = fernet.encrypt(password.encode())

    return encrypted_password


def input_email():          #to input the email
    global email
    email = input("Enter your Email: ")

def check_email():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'     #condition to check the email

    tries = None            #the local variable we will loop over

    while tries is not True:        #the loop till "tries" is true
        input_email()

        if(re.fullmatch(regex, email)):     #if the email satisfies all conditions, then "tries" is true, and the loop stops
            tries = True
            pass
        else:
            print("\n   Not a valid email, Try again...\n")      #if "tries" is false, it will loop over and over till a valid email is entered
            tries = False

def input_password():       #input password function
    global password
    password = input("Enter a password: ")

def password_checker():         #password checker function, the requirements are given on the start
    flag = 0

    tries = None            #the local variable we will loop over

    while tries is not True:
        input_password()        #the input password function inside the loop

        while True:

            #the requirements

            if (len(password)<=8):
                flag = -1
                break
                
            elif not re.search("[a-z]", password):
                flag = -1
                break
                
            elif not re.search("[A-Z]", password):
                flag = -1
                break
                
            elif not re.search("[0-9]", password):
                flag = -1
                break
                
            elif not re.search("[_@$]" , password):
                flag = -1
                break
        
            elif re.search(r"\s" , password):
                flag = -1
                break
            
            else:               #if all the requirements are fullfilled, the password will pass and they will be saved
                flag = 0
                tries = True
                encryption()
                break
    
        if flag == -1:          #if the password is not valid, it will loop over
            print("\n   Not a Valid Password, try again...")
            

def auto_password():
    question = [
        inquirer.List(
            "auto-generate",
            message="Do you want to auto generate the password?",
            choices=["Yes", "No"],
        )
    ]

    global answer
    answer = inquirer.prompt(question)

    if answer["auto-generate"] == "Yes":
        global password
        password = pg.generator()
    else:
        password_checker()

def info():             #the main function
    
    check_email()

    print("\n")

    auto_password()

    update()

if __name__ == "__main__":
    info()
