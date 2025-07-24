# import random

# # 🖼️ Array of ASCII art diagrams
# ascii_art_diagrams = [
#     r"""
#      /\_/\
#     ( o.o )
#      > ^ <
#     """,

#     r"""
#      _______
#     |       |
#     |       O
#     |      /|\
#     |      / \
#     |
#     =========
#     """,

#     r"""
#     _______
#    /       \
#   |  (• ◡•)  |
#    \_______/
#     """,

#     r"""
#      __
#     /  \
#    |    |
#    |____|
#   /      \
#  /________\
#     """
# ]

# # 📝 Array of creative writing prompts
# story_prompts = [
#     "Write a story about a robot who wants to be human.",
#     "Describe a world where plants can talk to people.",
#     "Create a mystery involving a time-traveling detective.",
#     "Tell a bedtime story set on a spaceship.",
#     "Imagine a dragon who’s afraid of fire.",
#     "Write about a kid who finds a magical notebook.",
#     "Narrate a short poem about loneliness and the moon.",
#     "Describe an ancient civilization powered by sound."
# ]

# # voter
# # if-else pair
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("Take a brake, touch some grass and come back when you're 18")

# # if-else code block
# if (age >= 18):{
#     print("You are eligible to vote.")
# }
# else:{
#     print("Take a brake, touch some grass and come back when you're 18")
# }
    
# # exercise: if a person is older than 16, they can play in the basketball field
# ager = int(input("Enter your player age: "))

# if ager > 16:
#     print("Get your gear and meeet us at the court")
# else:
#     print("Go home!")

# # elif (else-if) chain
# command = input("Enter 'exit' to end, enter 'continue' to not end: ")
# if command == "exit":
#     print("Exiting cmd")
# elif command == "continue":
#     print("Then continue...")
# else:
#     print("Write smth logical gdmit")

# # calculator

# first_number = float(input("Enter num1: "))
# second_number = float(input("Enter num2: "))
# operator = input("Enter operator sign: ")
# result = 0

# if operator=="+":
#     result = first_number + second_number
#     print(f"{first_number} + {second_number} = {result}")
# elif operator=="/":
#     if second_number == 0:
#         print("Math error")
#     else:
#         result = first_number / second_number
#         print(f"{first_number} / {second_number} = {result}")
# elif operator=="-":
#     result = first_number - second_number
#     print(f"{first_number} - {second_number} = {result}")
# elif operator=="%":
#     result = int(first_number) % int(second_number)
#     print(f"{first_number} mod {second_number} = {result}")
# elif operator=="*":
#     result = first_number * second_number
#     print(f"{first_number} * {second_number} = {result}")
# else:
#     print("Invalid operator")

# # leap year
# year = int(input("Enter year: "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year")
#         else:
#             print(f"{year} isn't a leap year")
#     else:
#         print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year.")

# if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#     print("Year is a leap year")
# else:
#     print("Year is not a leap year")