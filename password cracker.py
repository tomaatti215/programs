from random import *

user_pass = input("Enter your password: ")

crack = ""

password= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',]

while crack != user_pass:
    crack = ""
    for letter in range(len(user_pass)):
        crack_letter = password[randint(0, 25)]
        crack = str(crack_letter) + str(crack)
    print(crack)
print("Your password is: ", crack)