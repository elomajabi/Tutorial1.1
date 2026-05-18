# weak  if:
# less than 6 characters

# medium if:
# at least 6 characters
# contains only letters OR only numbers

# strong if:
# at least 8 characters
# contains letters AND numbers
# EXTRA CHECKS:
# whether it contains "@"
# whether it contains any digit

password = input("Please enter your password: ")
has_letter = any(char.isalpha() for char in password)
has_digit = any(char.isdigit() for char in password)
has_at = "@" in password

if len(password) < 6:
    print("Your password is weak")

elif len(password) >= 6 and (password.isalpha() or password.isdigit()):
    print("Your password is medium")

elif len(password) > 8 and has_letter and has_digit and has_at:
    print("Your password is strong")