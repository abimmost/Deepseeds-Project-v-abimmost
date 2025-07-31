def style():
    print("_" * 40)

def number_error():
    style()
    try:
        user_input = int(input("Please enter your phone number: "))
        print(f"User input: {user_input}")
    except ValueError:
        print(f"Incorrect number")

number_error()