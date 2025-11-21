import time
import hashlib
import os

# ===========================
# Ensure files are created next to this .py file
# ===========================
script_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_path)
print("Files will be created in:", script_path)

# ===========================
# Hashing function
# ===========================
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ===========================
# Load users from users.txt
# ===========================
def load_users():
    users = {}
    if os.path.exists("users.txt"):
        with open("users.txt", "r") as f:
            for line in f:
                if line.strip():
                    username, hashed_pw, attempts, lock_time = line.strip().split(",")
                    users[username] = {
                        "password": hashed_pw,
                        "attempts": int(attempts),
                        "lock_time": float(lock_time)
                    }
    return users

# ===========================
# Save users back to file
# ===========================
def save_users(users):
    with open("users.txt", "w") as f:
        for username, data in users.items():
            f.write(f"{username},{data['password']},{data['attempts']},{data['lock_time']}\n")

# ===========================
# Register Function
# ===========================
def register_user(users):
    while True:
        username = input("Enter a new username: ")

        if username in users:
            print("❌ Username already exists! Try another one.")
        else:
            break

    password = input("Enter a password: ")
    hashed_pw = hash_password(password)

    users[username] = {
        "password": hashed_pw,
        "attempts": 0,
        "lock_time": 0
    }

    save_users(users)
    print("✅ Registration successful!\n")

# ===========================
# Login Function with Per-User Lockout
# ===========================
def login_user(users):
    username = input("Enter username: ")

    if username not in users:
        print("❌ Username not found.")
        return

    user = users[username]

    # Check lockout
    current_time = time.time()
    if user["lock_time"] > current_time:
        remaining = int(user["lock_time"] - current_time)
        print(f"⏳ Account locked! Try again in {remaining} seconds.")
        return

    # Password check
    password = input("Enter password: ")
    hashed_pw = hash_password(password)

    if hashed_pw == user["password"]:
        print(f"🎉 Welcome back, {username}! Login successful.")
        user["attempts"] = 0
    else:
        user["attempts"] += 1
        print("❌ Incorrect password.")

        if user["attempts"] >= 3:
            user["lock_time"] = current_time + 120
            user["attempts"] = 0
            print("🔒 Too many attempts. Your account is locked for 120 seconds.")
    
    save_users(users)

# ===========================
# Main Menu
# ===========================
def main():
    users = load_users()

    while True:
        print("\n===== MENU =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register_user(users)
        elif choice == "2":
            login_user(users)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again.")

main()
