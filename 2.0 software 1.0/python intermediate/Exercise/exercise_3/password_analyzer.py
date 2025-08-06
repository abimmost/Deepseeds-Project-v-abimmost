# This function checks if the password meets all requirements
def check_string(s):
    while True:    
        # Flags to check each requirement
        upper = False
        lower = False
        digit = False
        special = False
        # Loop through each character in the password
        for char in s:
            if char.isupper():      # Check for uppercase letter
                upper = True
            elif char.islower():    # Check for lowercase letter
                lower = True
            elif char.isdigit():    # Check for digit
                digit = True
            elif char in "!@#$%^&*": # Check for special character
                special = True
        # If all requirements are met, return True
        if upper and lower and digit and special:
            return True
        else:
            # Print messages for missing requirements
            if not upper:
                print("Password must contain at least one uppercase letter.")
            if not lower:
                print("Password must contain at least one lowercase letter.")
            if not digit:
                print("Password must contain at least one digit.")
            if not special:
                print("Password must contain at least one special character: !@#$%^&*")
            break

# Main Program

# Loop until a valid password is entered
while True:
    # Show password requirements and get user input
    password = input("\nPassword Requirements:\n- 8 characters long\n- At least one uppercase\n- At least one lowercase\n- At least one digit\n- At least one special character: !@#$%^&*\n\nEnter your password:").strip()

    # Check if password is at least 8 characters long
    if len(password) < 8:
        print("Password must be at least 8 characters long.\n")
        continue
    else:
        # Check other requirements using the function
        if check_string(password):
            print("\nPassword is valid.")
            break