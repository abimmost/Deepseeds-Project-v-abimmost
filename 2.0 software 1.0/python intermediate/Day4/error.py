def style():
    print("_" * 40)

# def number_error():
#     style()
#     try:
#         user_input = int(input("Please enter your phone number: "))
#         print(f"User input: {user_input}")
#     except ValueError:
#         print(f"Incorrect number")

# number_error()

# def division_error():
#     try:
#         style()
#         f_num = int(input("Enter first number: "))
#         s_num = int(input("Enter second number: "))
#         return f_num/s_num
#     except ZeroDivisionError:
#         return "Enter a number different from zero"

# print(division_error())


# def dict_error(data):
#     # pass
#     try:
#         color = data['color']
#         print(f"My color is {color}")
#     except KeyError:
#         print("Color isn't a key")

# data = {
#     "name" : "Shimasu",
#     "age" : 23,
#     "favmeal" : "rice" 
# }

# dict_error(data)
# # print(dict_error())