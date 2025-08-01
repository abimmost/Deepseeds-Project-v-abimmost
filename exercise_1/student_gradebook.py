# Dictionary to store all students and their data
student_dictionary = {}

# Function to add a new student to the dictionary
def add_student(name):
    # Only add if the student doesn't already exist
    if name not in student_dictionary:
        student_dictionary[name] = {
            "average" : {
                "score" : 0,   # Placeholder for average score
                "grade" : ""   # Placeholder for grade (e.g. A, B)
            },
            "grade" : []       # List to store individual scores
        }
        print(f"Student {name} added successfully.")
    else:
        print("Name already exists")

# Function to get user input for student name
def names():
    name = input("Enter student's name: ").title()  # Capitalizes first letters
    return name

# Function to check if a student exists in the dictionary
def find_student(name):
    if name in student_dictionary:
        return name
    else:
        pass  # If not found, do nothing (returns None implicitly)

# Function to add multiple grades to a student
def add_grade(student):
    flag = 0  # Used to control when to stop adding grades
    score = 0
    print("Enter student grades one after the other     (Type '#' to exit):")
    while flag == 0:
        try:
            score = input("")
            if score == "#":
                flag = 1  # Exit the loop
            elif 0 <= int(score) <= 100:
                student["grade"].append(int(score))  # Add grade to list
            elif int(score) < 0 or int(score) > 100:
                print("Enter a grade between 0 and 100")  # Invalid grade
                continue
        except ValueError:
            print("Enter a valid integer")  # If input is not a number
    print(f"Grades added successfully for {len(student['grade'])} scores.")

# Function to determine letter grade based on score
def grade_avg(average):
    if 87 <= average <= 100:
        grade = "A+"
    elif 80 <= average <= 86:
        grade = 'A'
    elif 70 <= average <= 79:
        grade = 'B'
    elif 60 <= average <= 69:
        grade = 'C'
    elif 50 <= average <= 59:
        grade = 'D'
    elif 40 <= average <= 49:
        grade = 'E'
    else:
        grade = 'F'

    # Add + or - to grade if needed (except A+ or F)
    if 49 < average < 87:
        if 7 <= average % 10 <= 9:
            grade += '+'
        elif 0 <= average % 10 <= 2:
            grade += '-'
    return grade

# Function to calculate a student's average score and letter grade
def grade_avg_calc(student):
    total_score = sum(student["grade"])  # Add all grades
    if len(student["grade"]) > 0:
        student["average"]["score"] = (total_score / len(student["grade"])).__round__(2)  # Calculate average
        student["average"]["grade"] = grade_avg(student["average"]["score"] // 1)  # Get grade from score
    else:
        student["average"]["score"] = 0  # No grades entered
        student["average"]["grade"] = "N/A"

# Function to print a single student’s report
def student_report(student, name):
    grade_avg_calc(student)  # Make sure scores are calculated

    print(f"\nName: {name}\nAverage Score: {student['average']['score']}  (Grade: {student['average']['grade']})")
    print("Grades:", student["grade"])

# Function to display all students and class average
def display_all():
    for student in student_dictionary.values():
        grade_avg_calc(student)  # Update each student’s average and grade

    print("\nClass Statistics\n")
    if student_dictionary == {}:  # Check if any students exist
        print("No students in the gradebook.")
        return
    else:
        total_avg = 0
        for student in student_dictionary.values():
            total_avg += student["average"]["score"]  # Add up all student averages
        class_avg = total_avg / len(student_dictionary)  # Calculate class average
        for name, student in student_dictionary.items():
            print(f"Name: {name}, Average Score: {student['average']['score']} (Grade: {student['average']['grade']}), Grades: {student['grade']}")
        print(f"\nClass Average Score: {class_avg:.2f}\n")  # Show rounded class average

# ===== MAIN PROGRAM =====

print("\nTHE STUDENT GRADEBOOK\n")

# Infinite loop to keep the menu running
while True:
    scores = []  # Reset scores list (not actually used here)
    name = ""    # Reset name
    i = 0
    while i == 0:
        try:
            # Print the menu options
            print("\n1. Add Student\n2. Add Grade\n3. View Student Report\n4. Class Statistics\n5. Exit\n")
            choice = int(input("Choice: "))  # Get user choice
            i = 1  # Exit the input loop
        except ValueError:
            print("Incorrect format. Enter a number")  # If input is not an integer
    i = 0  # Reset for next menu cycle
    
    # Exit the program
    if choice == 5:
        print("\nSee you soon!")
        break

    # Add a new student
    elif choice == 1:
        add_student(names())

    # Add grades to a student
    elif choice == 2:
        name = names()
        if find_student(name):
            add_grade(student_dictionary[name])
        else:
            print("Name not found")
    
    # View individual student report
    elif choice == 3:
        name = names()
        if find_student(name):
            student_report(student_dictionary[name], name)
        else:
            print("Name not found")

    # View all students and class statistics
    elif choice == 4:
        display_all()