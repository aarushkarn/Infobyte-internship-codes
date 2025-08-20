import random
import string

def generate_password(length=12):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    if length < 12:
        print("Password length should be at least 12")
        return None
    
    password = ''.join(random.choice(all_characters) for i in range(length))
    
    return password

if __name__ == "__main__":
    password = generate_password()
    print(f"Generated Password: {password}")
