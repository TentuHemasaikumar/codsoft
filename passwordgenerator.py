import random
import string

def generate_password(length):
    if length < 1:
        return "Error: Password length must be at least 1."

    # Define the characters that can be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    if length < 1:
        print("The length of the password must be at least 1.")
        return

    password = generate_password(length)
    
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
