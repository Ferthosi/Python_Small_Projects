# ask user is they want to genrate a password or mot
# if they do , ask for password length
# genratepassword
# print password
# if initial response is no then exit program

'''import string
import random

characters = list(string.ascii_letters + string.digits+"!@#$%^&*()")

def generate_password():

    password_length= int(input("How long would you like your password to be "))

    random.shuffle(characters)
    password =[]
    for x in range(password_length):
        password.append(random.choice(characters))
    
    random.shuffle(password)

    password ="".join(password)

    print(password)

option = input("Do you want to genrate a password? (Yes/No): ")
if option == "Yes" or option=="yes":
    generate_password()
elif option =="No" or option == "no":
    print("Program ended")
    quit()
else:
    print("Invalid input, Please input yes or no")
    quit()'''

import string
import random

character = list(string.ascii_letters+string.digits+"!@#$%^&*()") 

def generate_password():

    password_length = int(input("How long would you want your password: "))

    random.shuffle(character)
    password =[]
    for x in range(password_length):
        password.append(random.choice(character))

    random.shuffle(password)

    password = "".join(password)
    
    print("Your password",password)

option = input("Do you want to generate a password? (Yes/No): ")

if option == "Yes" or option=="yes":
    generate_password()
elif option =="No" or option=="no":
    print("Program ended")
    quit()
else:
    print("Worng input, enter Yes or No")
    quit()