secret_password = "lion"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    guess = input("Guess the password: ")

    if guess == secret_password:
        print("Correct! Access granted.")
        break
    else:
        attempts += 1
        print("Wrong password. Attempts left:", max_attempts - attempts)

if attempts == max_attempts:
    print("Too many attempts. You are locked out!")