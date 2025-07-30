# print("Let's calculate BMI")
# def BMI_calc():
#     weight = float(input("Enter your weight: "))
#     h = float(input("Enter your height: "))
#     bmi = (weight)/(h * h)
#     if bmi <= 18 :
#         print(f"Your BMI is {bmi}. You are under weight")
#     elif 18 < bmi <= 25:
#         print(f"Your BMI is {bmi}. You are normal weight")
#     elif 25 < bmi <= 30:
#         print(f"Your BMI is {bmi}. You are over weight")
#     elif bmi > 30:
#         print("Your BMI is %.2f. You are obese" % (bmi))

# # print(BMI_calc())
# BMI_calc()

# print("Let's calculate BMI... again")
# def BMI_calc(ww, hh):
#     bmi = (ww)/(hh * hh)
#     if bmi <= 18 :
#         print(f"Your BMI is {bmi}. You are under weight")
#     elif 18 < bmi <= 25:
#         print(f"Your BMI is {bmi}. You are normal weight")
#     elif 25 < bmi <= 30:
#         print(f"Your BMI is {bmi}. You are over weight")
#     elif bmi > 30:
#         print("Your BMI is %.2f. You are obese" % (bmi))
# w = float(input("Enter your weight: "))
# h = float(input("Enter your height: "))

# BMI_calc(w,h)

# # BMI_calc()
# # print(BMI_calc())


# print("-" * 50,"Introduce Yourself\n","-" * 50)

# def create_profile(name, age ,occupation, city):
#     # message = print(f"Konichiwa. Watashi wa onamaewa {name}. {age} sai desu. {occupation} desu. {city} ni sundeimasu")
#     # message = (f"Konichiwa. Watashi wa onamaewa {name}. {age} sai desu. {occupation} desu. {city} ni sundeimasu")
#     message = f"Konichiwa. Watashi wa onamaewa {name}. {age} sai desu. {occupation} desu. {city} ni sundeimasu"
#     return message

# n = input("Enter your name: ")
# a = int(input("Enter your age: "))
# o = input("Enter your occupation: ")
# c = input("Enter your city: ")

# profile = create_profile(n, a, o, c)
# print(profile)

# def calculate_grade(score):
#     # def modifier(sco):
#     #     mod_digits_upper = ['7', '8', '9']
#     #     mod_digits_lower = ['0', '1', '2']
#     #     for i in range(0, 2, +1):
#     #         if mod_digits_lower[i] in str(sco):
#     #             mod_sign = '-'
#     #             return mod_sign
#     #         elif mod_digits_upper[i] in str(sco):
#     #             mod_sign = '+'
#     #             return mod_sign
#     #         else:
#     #             return
    
#     # mod_sign = modifier(score)
#     if 87 <= score <= 100:
#         grade = "A+"
#     elif 86 <= score <= 80:
#         grade = 'A'
#     elif 79 <= score <= 70:
#         grade = 'B'
#     elif 69 <= score <= 60:
#         grade = 'C'
#     elif 59 <= score <= 50:
#         grade = 'D'
#     elif 49 <= score <= 40:
#         grade = 'E'
#     else:
#         grade = 'F'

#     if 49 < score < 87:
#         if 7 <= score % 10 <= 9:
#             grade += '+'
#         elif 0 <= score % 10 <= 2:
#             grade += '-'
#     return grade

# # Test your function
# while True:
#     entry = input("Enter the score(0-100): \nType 'exit' to end")
#     if entry.strip().lower() == "exit":
#         break
#     elif entry.strip().isdigit():
#         score = int(entry)
#         if 0 <= score <= 100:
#             calculate_grade(score)
#         else:
#             print("Enter a proper score")

# print(f"Your grade is {calculate_grade} for score {score}")


# print("Shopping Cart Total Function\n""")
# def calculate_total(price, quantity, tax_rate=0.08):
#     """Calculate total cost including tax."""
#     # Your code here
#     # Calculate subtotal, tax amount, and final total
#     # Return the final total
#     subtotal = price * quantity
#     tax_amount = tax_rate * subtotal
#     final_total = subtotal + tax_amount
#     return final_total

# # Test your function
# # print("Type 'exit' for any of the inputs to end execution\n")
# p = float(input("Enter the price: "))
# q = float(input("Enter the quantity: "))
# total = calculate_total(p, q)
# print(f"Final price: {total:.2f} FCFA")