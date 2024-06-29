# password jenerator

import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    password = "".join(random.choice(characters) for i in range(length))
    return password

length = int(input("Enter the length of the password: "))
print("Generated Password : ", generate_password(length))