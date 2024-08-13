import random
import string

def generate_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    # Prompt the user for the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Length must be at least 1.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    # Generate and display the password
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
