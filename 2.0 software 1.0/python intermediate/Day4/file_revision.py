# PYTHON RECORD BOOK
# # Program that takes input from user and outputs with date and their output in a file


def record_in_file(text):
    # datetime.now().strftime("%Y-%m-%d")
    # current_time = datetime.now.strftime("%Y-%m-%d %H:%M")
    filename = "record.txt"
    try:
        with open("filename", "w") as file:
            file.write(f"TODAY'S DATE: {datetime.now().strftime("%Y-%m-%d")}")
            file.write(f"{text}\n")
    except FileNotFoundError:
        return "F"


from datetime import datetime
# try:
with open("record.txt", "w") as file:
    file.write("RECORD BOOK\n\n")

    print("// Type 'exit' to end\n")

    while True:  
        date_now = datetime.now().strftime("%Y-%m-%d %H:%M")
        print(f"TODAY'S DATE: {date_now}\n   NOTE:")
        text = input("")
        if text.strip().lower() == "exit":
            break
        else:
            file.write(f"TODAY'S DATE: {date_now}\n")
            file.write("   NOTE:\n      ")
            file.write(text + "\n\n")