# Password Analyzer Solution

This project solves the password analyzer problem by checking if a user's password meets specific requirements:

- Minimum length of 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character from `!@#$%^&*`

## Approach

The solution uses a function called `check_string` to validate the password. The function uses:

- **Boolean flags** to track if each requirement is met.
- **For loop** to iterate through each character in the password.
- **String methods** like `.isupper()`, `.islower()`, and `.isdigit()` to check character types.
- **Membership test** (`in`) to check for special characters.
- **Conditional statements** (`if`, `elif`, `else`) to set flags and print feedback.
- **While loop** in the main program to repeatedly prompt the user until a valid password is entered.
