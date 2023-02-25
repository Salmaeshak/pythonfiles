import re
def validate_password(password):
    regular_expression = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

    # compiling regex to create regex object
    pattern = re.compile(regular_expression)

    # searching regex
    valid = re.search(pattern, password)

    # validating conditions
    if valid:
        print("Password is valid.")
    else:
        print("Password is invalid.")
password = input("enter the password:")
validate_password(password)