## PASSWORD CHECKER

lower_case = upper_case = numeric = " "

password = input("Enter your password: ")

if len(password) > 7:
    for letter in password:
        if letter.islower():
            lower_case = letter
        if letter.isupper():
            upper_case = letter
        if letter.isdigit():
            numeric = letter
    
if lower_case and upper_case and numeric in password:
    print("Strong password")
else:
    print("Weak password")