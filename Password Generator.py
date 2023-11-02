import random

CHARS = "abcdefghijklmnopqrstuvwxyz"
UPPER_CHARS = CHARS.upper()
SYMBOLS = "!@#$%^&*()"

while 1:
    user_length = int(input(f"What is the length of the password you want to create? --> "))
    user_count  = int(input(f"How many passwords would you like to create? --> "))
    for x in range(0,user_count):
        password = ""
        for x in range(0,user_length):
            password_char = random.choice(CHARS + UPPER_CHARS + SYMBOLS)
            password      = password + password_char
        print(f"You password is : '{password}'")