# Correct email - classroom@gmail.com
# Correct password - 12345

email = input("Enter your email: ")

# checking if email contain @
if "@" in email:
    password = input("Enter your password: ")

    # both correct entries
    if email == "classroom@gmail.com" and password == "12345":
        print("Welcome")
    # password incorrect
    elif email == "classroom@gmail.com" and password != "12345":
        print("Wrong password")
        # one more chance
        password = input("Try Again ")
        # finally correct entry
        if password == "12345":
            print("Finally correct")
        else:
            print("Still Wrong password")
    else:
        print("Error in credentials")
else:
    print("Incorrect email, Enter Correct password")
    