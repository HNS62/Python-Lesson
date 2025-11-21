import hashlib
import os

# ============================
# Ensure files are saved next to this .py file
# ============================
script_path = os.path.dirname(os.path.abspath(__file__))  # Get folder where the script is
os.chdir(script_path)  # Change working directory to script folder
print("Files will be created in:", script_path)

# ============================
# Hash function
# ============================
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()  # Convert password to hash

# ============================
# Load users from file
# ============================
users_db = {}

if os.path.exists("users.txt"):
    with open("users.txt", "r") as file:
        for line in file:
            username, hashed_pass = line.strip().split(":")
            users_db[username] = hashed_pass
    print("📂 Users loaded from file.")
else:
    print("📂 No users.txt found. Starting fresh.")

# ============================
# Password Validation Rules
# ============================
special_chars = "!@#$%^&*()-_=+[]{}|;:',.<>/?"

# ============================
# Main Program
# ============================
print("=== Welcome to Secure Program ===")

while True:
    print("\n--- Main Menu ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter 1, 2, or 3: ")

    # Validate menu choice
    if choice not in ["1", "2", "3"]:
        print("❌ Invalid choice. Please enter 1, 2, or 3.")
        continue

    # ---------------------
    # REGISTER
    # ---------------------
    if choice == "1":
        print("\n=== Registration ===")

        # Username validation
        while True:
            username = input("Enter username: ")
            if username in users_db:
                print("❌ Username already exists. Try another.")
            else:
                break  # Valid username

        # Password validation
        while True:
            password = input("Enter password: ")

            if len(password) < 8:
                print("❌ Password too short, must be 8+ characters.")
            elif not any(char.isupper() for char in password):
                print("❌ Password must have at least one uppercase letter.")
            elif not any(char.isdigit() for char in password):
                print("❌ Password must include at least one number.")
            elif not any(char in special_chars for char in password):
                print("❌ Password must include at least one special character.")
            else:
                print("✅ Password is strong!")
                break  # Valid password

        # Hash password and save
        hashed_pass = hash_password(password)
        users_db[username] = hashed_pass

        with open("users.txt", "a") as file:
            file.write(f"{username}:{hashed_pass}\n")

        print("✅ Registration successful and saved.")

    # ---------------------
    # LOGIN (Session 12)
    # ---------------------
    elif choice == "2":
        print("\n=== Login ===")

        username = input("Enter username: ")

        # Check if user exists
        if username not in users_db:
            print("❌ Username does not exist.")
            continue

        # Attempt counter
        attempts = 0

        # Allow max 3 attempts
        while attempts < 3:
            password = input("Enter password: ")
            hashed_pass = hash_password(password)

            if users_db[username] == hashed_pass:
                print(f"✅ Welcome back, {username}! Login successful.")
                break
            else:
                attempts += 1
                print(f"❌ Wrong password. Attempts left: {3 - attempts}")

        # If 3 failures → lockout
        if attempts >= 3:
            print("⛔ Too many attempts. You are locked out.")

    # ---------------------
    # EXIT
    # ---------------------
    elif choice == "3":
        print("👋 Program closed. Goodbye!")
        break
