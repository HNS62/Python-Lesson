secret_password = "lion"
guess = ""

while guess != secret_password:
    guess = input("Guess the password: ")

print("Correct! You cracked the password!")