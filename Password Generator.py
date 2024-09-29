import random
from random import shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the password generator made by Sahul")
sh_letters = int(input("How many letters would you like in your password?\n"))
sh_numbers = int(input("How many numbers would you like in your password?\n"))
sh_symbols = int(input("How many symbols would you like in your password?\n"))

password_list = []

for _ in range(sh_numbers):
    password_list.append(random.choice(letters))

for _ in range(sh_numbers):
    password_list.append(random.choice(numbers))

for _ in range(sh_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
password = ''.join(password_list)

print(f"Your password is {password}")