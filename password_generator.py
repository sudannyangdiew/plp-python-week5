# Question 1 - Password Generator

import random
import string


def make_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ""
    for i in range(length):
        # Add one random character from characters onto the end of password
        password += random.choice(characters)
    return password


# Generate p1 using default length (8) and p2 with length 12
p1 = make_password()
p2 = make_password(12)

print("Password:", p1)
print("Length:", len(p1))
print("Password:", p2)
print("Length:", len(p2))