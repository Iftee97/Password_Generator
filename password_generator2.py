# password generator project
# Angela's solution:

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# easy password:
# --------------

letter_password = ""
for char in range(1, nr_letters + 1):
    letter_password += random.choice(letters)

number_password = ""
for char in range(1, nr_numbers + 1):
    number_password += random.choice(numbers)

character_password = ""
for char in range(1, nr_symbols + 1):
    character_password += random.choice(symbols)

final_password = letter_password + number_password + character_password
print(f"final password: {final_password}")


# ------------------------------------------------------------------------------------------------------------------


# hard password
# -------------

# password_list = []

# letter_password = ""
# for char in range(1, nr_letters + 1):
#     password_list.append(random.choice(letters))

# number_password = ""
# for char in range(1, nr_numbers + 1):
#     password_list.append(random.choice(numbers))

# character_password = ""
# for char in range(1, nr_symbols + 1):
#     password_list.append(random.choice(symbols))


# random.shuffle(password_list)

# final_password = ''.join(password_list)
# print(f"final password: {final_password}")