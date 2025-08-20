import random
import string

def generate_password():
    # User input for password length
    length = int(input("Enter the length of the password: "))

    # User choice for character sets
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include special characters? (y/n): ").lower() == 'y'

    # Build character pool
    characters = ""
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Ensure user selected at least one character type
    if not characters:
        return "Error: You must select at least one character type!"

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Run
print("Generated Password:", generate_password())