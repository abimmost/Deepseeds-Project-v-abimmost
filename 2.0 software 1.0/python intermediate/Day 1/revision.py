# print("Let's FizzBuzz")
# while True:
#     number = input("Enter a number(enter 'exit' to end): ")
#     if number.strip().lower() == "exit":
#         break
#     elif number.strip().isdigit():
#         num = int(number)
#         if num % 3 == 0 and num % 5 == 0:
#             print("FizzBuzz")
#         elif num % 5 == 0:
#             print("Buzz")
#         elif num % 3 == 0:
#             print("Fizz")
#         else:
#             print(num)
#     else:
#         print("Enter a valid response")

# print("Swapper")
# while True:
#     a = input("Enter value for A(Type 'exit' to end): ")
#     b = input("Enter value for B(Type 'exit' to end): ")
#     if a.strip().lower() or b.strip().lower() == "exit":
#         break
#     elif a.strip().isdigit() and b.strip().isdigit():
#         c=a
#         a=b
#         b=c
#         print(f"\nABracAdaBRAA🪄\nA = {a}, B = {b}")
#     else:
#         print("Enter valid response")

# import random
# print("Guess the number(By Range)\n")
# while True:
#     status = input("1.Play      2.Exit: ")
#     if status.strip().lower() == "1" or status.strip().lower() == "play":
#         # range = 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
#         randnum = random.randint(1,20)
#         print("I have my number. What's your guess? ")
#         i = 3
#         while i > 0:
#             guess = int(input(f"Guess the number({i} tries left): "))
#             if guess > randnum:
#                 print("Above my guess")
#             elif guess < randnum:
#                 print("Below my guess")
#             elif guess == randnum:
#                 print("WINNER!🏆")
#                 break
#             elif i == 0:
#                 print(f"My guess was {guess}. Try harder next time 😉")
#                 break
#             i -= 1
#     elif status.strip().lower() == "2" or status.strip().lower() == "exit":
#         print("Until next time 👋")
#         break