#the requiements of the password:
#   1. at least 8 characters
#   2. at least one lower case character
#   3. at least one upper case character
#   4. at least one number
#   5. at least one special character($ or _ or @)

import string
import random
import inquirer

def password_length():
    global length
    length = int(input("Enter password length: "))
    
    if length < 8:
        print("\n   Password length should be at-least 8 characters")
        password_length()
    
    return length

def password_type():
    question = [
        inquirer.List(
            "choice",
            message="Choose a character set for password from these:",
            choices=["Digits", "Letters", "Special characters", "Mix of above three", "Exit"]
        )
    ]

    global answers

    answers = inquirer.prompt(question)  

    return answers

def satisfaction():
    question = [
        inquirer.List(
            "satisfaction",
            message="Do you want to generate another password?",
            choices=["Yes", "No"]
        )
    ]

    answers.update(inquirer.prompt(question))

    if answers["satisfaction"] == "No":
        pass
    else:
        generator()

def checker():
    global password

    characterList = ""
    password = []
 
    if(answers["choice"] == "Letters"):
        # Adding letters to possible characters
        characterList += string.ascii_letters
        
    elif(answers["choice"] == "Digits"):     
        # Adding digits to possible characters
        characterList += string.digits
    
    elif(answers["choice"] == "Special characters"):         
        # Adding special characters to possible
        # characters
        characterList += string.punctuation

    elif(answers["choice"] == "Mix of above three"):
        #add all the characters and digits in the mix
        characterList += string.ascii_letters + string.digits + string.punctuation

    elif(answers["choice"] == "Exit"):
        exit()
 
    for i in range(length):
   
        # Picking a random character from our 
        # character list
        randomchar = random.choice(characterList)
     
        # appending a random character to password
        password.append(randomchar)
 
    # printing password as a string
    print("The random password is " + "".join(password),"\n")

    satisfaction()

    global auto_password
    auto_password = "".join(password)

    return auto_password

def generator():
    
    password_length()
    
    password_type()

    checker()

    return auto_password

if __name__ == "__main__":
    generator()