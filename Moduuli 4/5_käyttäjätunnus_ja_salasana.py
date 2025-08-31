attempts = 0

while True:
    attempts += 1
    username = input("Enter username: ")
    password = input("Enter password: ")

    if attempts == 5:
        print("Access denied")
        break

    elif username == "python" and password == "rules":
        print("Welcome")
        break

    elif username != "python" and password != "rules":
        print("Incorrect username or password. Please try again.")