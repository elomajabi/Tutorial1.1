# @ , .com , no spaces

while True:
    email = input("Enter your email: ")

    if "@" in email and ".com" in email and not " " in email:
        print("Valid email")
        break

    else:
        print("Invalid email")