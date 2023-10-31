# Correct email - classroom@gmail.com
# Correct password - 12345

email = input("Enter your email: ")
if "@" in email:
    password = input("Enter your password: ")

    if email == "classroom@gmail.com" and password == "12345":
        print("Welcome")
    elif email == "classroom@gmail.com" and password != "12345":
        print("Wrong password")
        password = input("Try Again ")
        if password == "12345":
            print("Finally correct")
        else:
            print("Still Wrong password")
    else:
        print("Error in credentials")
else:
    print("Incorrect email, Enter Correct password")
    