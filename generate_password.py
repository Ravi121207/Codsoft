import random
import string

def generate_password(length):
    if length < 4:
        return "password length must be  at least 4 characters"
    all_chars=string.ascii_letters + string.digits + string.punctuation
    
    password=[
        random.choice(string.ascii_letters),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    password +=[random.choice(all_chars) for _ in range(length - 3)]
    
    random.shuffle(password)
    return ''.join(password)
print(generate_password(int(input("Enter the password length: "))))