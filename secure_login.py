correct_user = "nader"
correct_pass = "1234"
attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_user and password == correct_pass:
        print("Login successful!")
        break
    else:
        attempts -= 1
        print("Access denied. Attempts left:", attempts)