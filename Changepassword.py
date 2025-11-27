import os
import time
import hashlib

# ============================
# Ensure files are saved next to this .py file
# ============================
script_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_path)
print("Files will be created in:", script_path)

# ============================
# Password hashing function
# ============================
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ============================
# Load users from file
# ============================
def load_users():
    users = {}
    if os.path.exists("users.txt"):
        with open("users.txt", "r") as f:
            for line in f:
                username, password, attempts, lock_time = line.strip().split(",")
                users[username] = {
                    "password": password,
                    "attempts": int(attempts),
                    "lock_time": float(lock_time)
                }
    return users

# ============================
# Save users to file
# ============================
def save_users(users):
    with open("users.txt", "w") as f:
        for username, data in users.items():
            f.write(f"{username},{data['password']},{data['attempts']},{data['lock_time']}\n")

# ============================
# Registration function
# ============================
def register_user():
    users = load_users()

    while True:
        username = input("Enter a username: ").strip()
        if username in users:
            print("Username already exists. Please choose another one.")
        else:
            break

    password = input("Enter a password: ").strip()
    hashed_pw = hash_password(password)

    users[username] = {
        "password": hashed_pw,
        "attempts": 0,
        "lock_time": 0
    }

    save_users(users)
    print("Registration successful!")

# ============================
# Login function
# ============================
def login_user():
    users = load_users()

    username = input("Enter your username: ").strip()

    if username not in users:
        print("Username does not exist.")
        return None  # no user logged in

    user = users[username]

    # Check lock
    if user["attempts"] >= 3:
        time_passed = time.time() - user["lock_time"]
        if time_passed < 120:
            print("Account locked. Try again later.")
            return None
        else:
            user["attempts"] = 0

    password = input("Enter your password: ").strip()
    hashed_pw = hash_password(password)

    if hashed_pw == user["password"]:
        print("Login successful!")
        user["attempts"] = 0
        save_users(users)
        return username  # logged-in user

    else:
        user["attempts"] += 1
        if user["attempts"] >= 3:
            user["lock_time"] = time.time()
            print("Too many attempts. Account locked for 120 seconds.")
        else:
            print("Incorrect password.")

        save_users(users)
        return None

# ============================
# Change Password function (NEW)
# ============================
def change_password(username):
    users = load_users()
    user = users[username]

    old_pw = input("Enter your old password: ").strip()

    if hash_password(old_pw) != user["password"]:
        print("Old password is incorrect.")
        return

    new_pw = input("Enter your new password: ").strip()
    confirm = input("Confirm new password: ").strip()

    if new_pw != confirm:
        print("Passwords do not match.")
        return

    if new_pw == old_pw:
        print("New password cannot be the same as old password.")
        return

    user["password"] = hash_password(new_pw)
    save_users(users)
    print("Password updated successfully!")

# ============================
# Main program loop
# ============================
while True:
    print("\n===== MENU =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        register_user()

    elif choice == "2":
        logged_user = login_user()

        if logged_user:
            print(f"\nWelcome, {logged_user}!")

            while True:
                print("\n----- User Menu -----")
                print("1. Change Password")
                print("2. Logout")

                sub_choice = input("Choose an option: ").strip()

                if sub_choice == "1":
                    change_password(logged_user)

                elif sub_choice == "2":
                    print("Logged out.")
                    break

                else:
                    print("Invalid choice.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
