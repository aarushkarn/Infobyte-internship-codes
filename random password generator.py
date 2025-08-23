import random
import string

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    if length < 12:
        print("Password  slength should be at least 12")
        return None
    
    password = ''.join(random.choice(all_characters) for i in range(length))
    
    return password

if __name__ == "__main__":
    user_length = int(input("Enter password length (minimum 12): "))
    password = generate_password(user_length)
    print(f"Generated Password: {password}")
