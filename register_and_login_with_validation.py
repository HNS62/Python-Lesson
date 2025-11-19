import hashlib

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Users "database" (username: hashed_password)
users_db = {}

print("=== Welcome to the Secure Program ===")

while True:
    print("\n--- Main Menu ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter 1, 2, or 3: ")

    # ---------------------
    # Input validation
    # ---------------------
    if choice not in ["1", "2", "3"]:
        print("❌ Invalid choice. Please enter 1, 2, or 3.")
        continue

    # ---------------------
    # REGISTER
    # ---------------------
    if choice == "1":
        print("\n=== Registration ===")

        # Keep asking for a unique username
        while True:
            username = input("Enter username: ")
            if username in users_db:
                print("❌ Username already exists. Try another.")
            else:
                break

        password = input("Enter password: ")
        hashed_pass = hash_password(password)

        users_db[username] = hashed_pass
        print("✅ Registration successful.")

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