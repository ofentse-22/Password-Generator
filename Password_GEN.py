import random 
import string 

def generate_password( min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    Characters = letters
    if numbers:
        Characters += digits
    if special_characters:
        Characters += special

    PassW = "" 
    meets_requirements = False
    has_number = False
    has_special = False

    while not meets_requirements or len(PassW) < min_length:
        new_char = random.choice(Characters)
        PassW += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_requirements = True
        if numbers:
            meets_requirements = has_number
        if special_characters:
            meets_requirements = meets_requirements and has_special


    return PassW    
min_length = int(input("Enter the minimum length for the password: "))
has_numbers = input("Include numbers? (y/n): ")
has_special = input("Include special characters? (y/n): ")
PassW = generate_password(min_length, numbers=has_numbers == 'y', special_characters=has_special == 'y')
print("The generated password is:", PassW)