import hashlib
import os

# ============================
# Ensure files are saved next to this .py file
# ============================
script_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_path)
print("Files will be created in:", script_path)

# ============================
# Hash function
# ============================
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

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
# Main program
# ============================
print("=== Welcome to Secure Program ===")

while True:
    print("\n--- Main Menu ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter 1, 2, or 3: ")

    # Validate choice
    if choice not in ["1", "2", "3"]:
        print("❌ Invalid choice. Please enter 1, 2, or 3.")
        continue

    # ---------------------
    # REGISTER
    # ---------------------
    if choice == "1":
        print("\n=== Registration ===")

        # Ask until username is unique
        while True:
            username = input("Enter username: ")
            if username in users_db:
                print("❌ Username already exists. Try another.")
            else:
                break

        password = input("Enter password: ")
        hashed_pass = hash_password(password)

        # Save to dictionary
        users_db[username] = hashed_pass

        # Save to file
        with open("users.txt", "a") as file:
            file.write(f"{username}:{hashed_pass}\n")

        print("✅ Registration successful and saved.")

    # ---------------------
    # LOGIN
    # ---------------------
    elif choice == "2":
        print("\n=== Login ===")
        username = input("Enter username: ")
        password = input("Enter password: ")
        hashed_pass = hash_password(password)

        if username in users_db and users_db[username] == hashed_pass:
            print(f"✅ Welcome back, {username}! Login successful.")
        else:
            print("❌ Incorrect username or password.")

    # ---------------------
    # EXIT
    # ---------------------
    elif choice == "3":
        print("👋 Program closed. Goodbye!")
        break
