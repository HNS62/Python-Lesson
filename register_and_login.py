import hashlib

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Our "database" of users
users = []

while True:
    print("\nChoose an option:")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter 1, 2, or 3: ")

    # REGISTER
    if choice == "1":
        username = input("Choose a username: ")
        password = input("Choose a password: ")

        hashed_pass = hash_password(password)

        users.append({"username": username, "password": hashed_pass})

        print("User created successfully!")

    # LOGIN
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")

        hashed_pass = hash_password(password)

        login_success = False

        for user in users:
            if user["username"] == username and user["password"] == hashed_pass:
                login_success = True
                break

        if login_success:
            print(f"Welcome back, {username}! Login successful.")
        else:
            print("Incorrect username or password.")

    # EXIT
    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option, try again.")