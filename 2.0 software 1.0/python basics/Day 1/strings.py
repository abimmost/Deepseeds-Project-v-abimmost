# ### STRINGS

## INTERPOLATION**: Putting variables inside print strings
# print(f"The temperature {celcius} Celcius is {fahrenheit} Fahrenheit")

## concatenation
# combine_name=name + one_char

## repetition
# print(f"{"Hello " * 7}") # prints Hello seven times

## multiline_string
# multiline_string = """good
# morniong
# shiii"""
# print(multiline_string)

## length of a string
# message = "What de fun"
# print(len(message))

## character psoition in a string
# print(f"The fourth character is {message[5]}")

## string formatting

# names="alucard mcGregor"
# age=408
# score=28.4
# # method 1: f-strings (recommended - like fill-in-the-blanks)
# print(f"Hello, {names}! You are {age} years old!\nYour score is {score: .2f}%")

# # method 2: .format() method
# print("Hello, {}! You are {} years old." .format(names, age))

# # method 3: % formatter (older, convert-like style)
# print("Hello, %s! You are %d years old!" % (names, age))
# print(names.strip().startswith("alucard"))
# print(names.title())
# print(names.split())
# print("-".join(names))
# print(names.startswith(" "))
# print("mc" in names)

## String Project: Email separate
# email = "user@example.com"
# email2 = input("Enter your email: ")
# if "@" and "." in email:
#     username = email.split("@")[0]
#     domain = email.split("@")[1]
#     print(f"Username: {username}")
#     print(f"Domain: {domain}")
# else:
#         print("Invalid email format")