student_dictionary = {}


def add_student(name):
    if name not in student_dictionary:
        student_dictionary[name] = {
            "average" : {
                "score" : 0,
                "grade" : ""
            },
            "grade" : []
        }
        print(f"Student {name} added successfully.")
    else:
        print("Name already exists")

def names():
    name = input("Enter student's name: ").title()
    return name

def find_student(name):
    if name in student_dictionary:
        return name
    else:
        pass

def add_grade(student):
    flag = 0
    score = 0
    print("Enter student grades one after the other     (Type '#' to exit):")
    while flag == 0:
        try:
            score = input("")
            if score == "#":
                flag = 1
            elif 0 <= int(score) <= 100:
                student["grade"].append(int(score))
            elif int(score) < 0 or int(score) > 100:
                print("Enter a grade between 0 and 100")
                continue
        except ValueError:
            print("Enter a valid integer")
    print(f"Grades added successfully for {len(student['grade'])} scores.")

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

    if 49 < average < 87:
        if 7 <= average % 10 <= 9:
            grade += '+'
        elif 0 <= average % 10 <= 2:
            grade += '-'
    return grade

def grade_avg_calc(student):
    total_score = sum(student["grade"])
    if len(student["grade"]) > 0:
        student["average"]["score"] = (total_score / len(student["grade"])).__round__(2)
        student["average"]["grade"] = grade_avg(student["average"]["score"] // 1)
    else:
        student["average"]["score"] = 0
        student["average"]["grade"] = "N/A"

def student_report(student, name):
    grade_avg_calc(student)

    print(f"\nName: {name}\nAverage Score: {student['average']['score']}  (Grade: {student['average']['grade']})")
    print("Grades:", student["grade"])

def display_all():
    for student in student_dictionary.values():
        grade_avg_calc(student)

    print("\nClass Statistics\n")
    if student_dictionary == {}:
        print("No students in the gradebook.")
        return
    else:
        total_avg = 0
        for student in student_dictionary.values():
            total_avg += student["average"]["score"]
        class_avg = total_avg / len(student_dictionary)
        for name, student in student_dictionary.items():
            print(f"Name: {name}, Average Score: {student['average']['score']} (Grade: {student['average']['grade']}), Grades: {student['grade']}")
        print(f"\nClass Average Score: {class_avg:.2f}\n")


# Main code
print("\nTHE STUDENT GRADEBOOK\n")

while True:
    
    scores = []
    name = ""
    i = 0
    while i == 0:
        try:
            print("\n1. Add Student\n2. Add Grade\n3. View Student Report\n4. Class Statistics\n5. Exit\n")
            choice = int(input("Choice: "))
            i = 1
        except ValueError:
            print("Incorrect format. Enter a number")
    i = 0
    
    if choice == 5:
        print("\nSee you soon!")
        break

    elif choice == 1:
        add_student(names())

    elif choice == 2:
        name = names()
        if find_student(name):
            add_grade(student_dictionary[name])
        else:
            print("Name not found")
    
    elif choice == 3:
        name = names()
        if find_student(name):
            student_report(student_dictionary[name], name)
        else:
            print("Name not found")

    elif choice == 4:
        display_all()