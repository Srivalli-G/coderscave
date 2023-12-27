import secrets
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    lowercase_letter = secrets.choice(string.ascii_lowercase)
    uppercase_letter = secrets.choice(string.ascii_uppercase)
    digit = secrets.choice(string.digits)
    symbol = secrets.choice(string.punctuation)
    remaining_length = length - 4 
    password = (
        lowercase_letter
        + uppercase_letter
        + digit
        + symbol
        + ''.join(secrets.choice(characters) for _ in range(remaining_length))
    )
    password_list = list(password)
    secrets.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password
password = generate_password(10)
print("Generated Password:", password)