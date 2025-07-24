# # import random

# # target = random.randint(1, 10)
# # guess = 0
# # attempts = 0

# # print("I'm thinking of a number between 1 and 10...")
# # while guess != target and attempts < 3:
# #     guess = int(input("Please enter your guess: ")) # Simulating user guess
# #     attempts += 1

# #     if guess == target:
# #         print(f"Correct! The number was {target}")
# #         print(f"It took {attempts} attempts")
# #     elif guess < target:
# #         print(f"Guess {guess} is too low")
# #     else:
# #         print(f"Guess {guess} is too high")

# # if guess != target:
# #     print(f"Sorry! The number was {target}")


# # Password validator
# # def validate_password(password):
# #     has_upper = False
# #     has_lower = False
# #     has_digit = False

# #     for char in password:
# #         if char.isupper():
# #             has_upper = True
# #         elif char.islower():
# #             has_lower = True
# #         elif char.isdigit():
# #             has_digit = True

# #     return has_upper and has_lower and has_digit and len(password) >= 8

# # # Test passwords
# # passwords = ["Password123", "password", "PASSWORD", "Pass123"]
# # for pwd in passwords:
# #     if validate_password(pwd):
# #         print(f"'{pwd}' is a strong password ✓")
# #     else:
# #         print(f"'{pwd}' is a weak password ✗")

# password=input("Please enter your password: ")
# has_lower=False
# has_upper=False
# has_digits=False
# # check if password is weak or strong:
# # strong password should contain caps, lower and digits
# # islower(), isupper(), isdigit()
# for pwd in password:
#     if pwd.isupper():
#         has_upper=True
#     elif pwd.islower():
#         has_lower=True
#     elif pwd.isdigit():
#         has_digits=True
# if has_digits and has_lower and has_upper:
#     print(f"It was indeed a strong password: {password}")
# else:
#     print("That password was very weak")

    


# Multiplication table
# print("Multiplication Table:")
# for i in range(1, 12):  # Rows
#     print("__"*45)

#     for j in range(1, 12):  # Columns
#         result = i * j
#         print(f"{i} x {j} = {result}")
#     print()  # Empty line after each row

# age = 25
# has_license = True
# has_insurance = True

# # AND operator (all conditions must be True)
# if age >= 18 and has_license and not has_insurance:
#     print("You can drive!")
# else:
#     print("Cannot drive.....")


# OR operator (at least one condition must be True)
# is_weekend = False
# is_holiday = True

# if is_weekend or is_holiday:
#     print("No work today!")


# is_raining = False
# if not is_raining:
#     print("Let's go for a walk!")

# # BASICS

# names = ["Atsimbom", "Shambom", "Abt", "Simbomgrl", "Sugoiu"]

# FORLOOP
# for name in names:
#     if name.endswith("mbom"):
#         print(f"{name} you are under arrest")
#     else:
#         print(f"{name}, carry on model citizen")

# i = 1
# for name in names:
#     print(f"{i}. {name}")
#     i += 1

# range
# for i in range(5):
#     print(i)

#range(start, stop)
# for i in range(2,7):
#     print(i)

# range(start, stop, step)
# for i in range(0,10,2):
#     print(i)

# Coutndown
# for i in range(10,0,-1):
#     print(f"Countdown: {i}")
# print("Leshh gooo!😊")

# WHILELOOP

# Basic while loop
# count = 1
# while count <= 5:
#     print(f"{count}. madness")
#     count += 1

# User input loop
# user_input = ""

# while user_input != "quit":
#     user_input = input("Enter 'quit' to exit: ")
#     print(f"You entered {user_input}")
# print("Goodbye")

# Break keyword - finding first even number
# print("finding the first even number\n")
# for number in range(1,10):
#     if number % 2 == 0:
#         print(f"First even number found: '{number}'")
#         break
#     print(f"'{number}' is odd")

# continue keyword - finding all oddies
# for number in range(1,10):
#     if number % 2 == 0:
#         continue
#     print(f"Odd found: '{number}'")

# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    # print()

# Triangle pattern
for row in range(1, 6):
    for star in range(row):
        print("*", end=" ")
    print()