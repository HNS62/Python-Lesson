import hashlib
import os
import time

# =====================================
# Load and Save Users
# =====================================
def load_users():
    users = {}
    if os.path.exists("users.txt"):
        with open("users.txt", "r") as f:
            for line in f:
                if line.strip():
                    username, hashed_pw = line.strip().split(",")
                    users[username] = hashed_pw
    return users

def save_users(users):
    with open("users.txt", "w") as f:
        for username, pw in users.items():
            f.write(f"{username},{pw}\n")

# =====================================
# Password Hashing
# =====================================
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# =====================================
# GLOBAL LOCK VARIABLES
# =====================================
GLOBAL_ATTEMPTS = 0
GLOBAL_LOCK_TIME = 0

# =====================================
# Register Function
# =====================================
def register_user(users):
    while True:
        username = input("Choose a username: ").strip()
        if username in users:
            print("This username already exists. Try another one.")
            continue
        break

    password = input("Choose a password: ").strip()
    hashed_pw = hash_password(password)

    users[username] = hashed_pw
    save_users(users)

    print("User registered successfully!")

# =====================================
# Login Function (GLOBAL LOCK)
# =====================================
def login_user(users):
    global GLOBAL_ATTEMPTS, GLOBAL_LOCK_TIME

    # 1️⃣ check if system is locked
    current_time = time.time()
    if current_time < GLOBAL_LOCK_TIME:
        wait_seconds = int(GLOBAL_LOCK_TIME - current_time)
        print(f"System Locked. Try again in {wait_seconds} seconds.")
        return

    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if username not in users:
        print("Username not found.")
        GLOBAL_ATTEMPTS += 1
    else:
        hashed_pw = hash_password(password)
        if hashed_pw == users[username]:
            print(f"Welcome, {username}! Login successful.")
            GLOBAL_ATTEMPTS = 0
            return
        else:
            print("Incorrect password.")
            GLOBAL_ATTEMPTS += 1

    # 2️⃣ Lock the entire system if 3 wrong attempts
    if GLOBAL_ATTEMPTS >= 3:
        GLOBAL_LOCK_TIME = time.time() + 120
        GLOBAL_ATTEMPTS = 0
        print("Too many failed attempts! System locked for 120 seconds.")

# =====================================
# Main Menu
# =====================================
def main():
    users = load_users()

    while True:
        print("\n--- MENU ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            register_user(users)
        elif choice == "2":
            login_user(users)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

main()
