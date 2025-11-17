users = [
    {"username": "nader", "password": "1234"},
    {"username": "ahmed", "password": "abcd"},
    {"username": "sara", "password": "pass"}
]

max_attempts = 3
attempts = 0

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    login_success = False
    
    for user in users:
        if user["username"] == username and user["password"] == password:
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
