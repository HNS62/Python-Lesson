import hashlib

# Function to hash a password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Users database with hashed passwords
users = [
    {"username": "nader", "password": hash_password("1234")},
    {"username": "ahmed", "password": hash_password("abcd")},
    {"username": "sara", "password": hash_password("pass")}
]

max_attempts = 3
attempts = 0

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    hashed_input = hash_password(password)
    login_success = False
    
    for user in users:
        if user["username"] == username and user["password"] == hashed_input:
            login_success = True
            break

    if login_success:
        print(f"Welcome, {username}! Login successful.")
        break
    else:
        attempts += 1
        print("Access denied. Attempts left:", max_attempts - attempts)

if attempts == max_attempts:
    print("Too many attempts. You are locked out!")
