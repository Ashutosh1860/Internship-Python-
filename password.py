import random
import string

def generate_password(length, include_lowercase=True, include_uppercase=True, include_digits=True, include_symbols=True):
    characters = ''
    
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: No character set selected for password generation.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    # Get user input for password criteria
    length = int(input("Enter the length of the password: "))
    include_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    include_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    include_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

    # Generate the password
    password = generate_password(length, include_lowercase, include_uppercase, include_digits, include_symbols)

    # Display the generated password
    if password:
        print("Generated Password:", password)
    else:
        print("Password generation failed.")

if __name__ == "__main__":
    main()
