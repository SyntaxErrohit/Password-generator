import random
import string

def generate(length, numbers=True, spl_char=False):
    alpha = string.ascii_letters
    digits = string.digits
    punc = string.punctuation

    characters = alpha
    if numbers:
        characters += digits
    if spl_char:
        characters += punc

    password = ""
    for i in range(length):
        ch = random.choice(characters)
        while ch in password:
            ch = random.choice(characters)
        password += ch
    
    return password

passwd = generate(10, True, True)
print(passwd)