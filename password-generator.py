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
    met_condn = False
    has_num = False
    has_spl = False
    while not met_condn or len(password) < length:
        c = random.choice(characters)
        while c in password:
            c = random.choice(characters)
        password += c

        if c in digits:
            has_num = True
        elif c in punc:
            has_spl = True

        met_condn = True
        if numbers:
            met_condn = has_num
        
        if spl_char:
            met_condn = met_condn and has_spl

    return password

passwd = generate(10, False, False)
print(passwd)
