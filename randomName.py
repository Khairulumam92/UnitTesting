import random
import string

def generate_random_name():
    first_names = ["John", "Jane", "Alex", "Emily", "Chris", "Katie"]
    last_names = ["Smith", "Doe", "Johnson", "Brown", "Davis", "Miller"]
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return f"{first_name} {last_name}"

def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Example usage
if __name__ == "__main__":
    print("Random Name:", generate_random_name())
    print("Random Password:", generate_random_password())
