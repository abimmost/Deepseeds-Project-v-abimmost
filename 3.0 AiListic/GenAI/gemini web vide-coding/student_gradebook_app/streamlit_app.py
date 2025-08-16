import streamlit as st

# Initialize student_dictionary in session_state if it doesn't exist
if 'student_dictionary' not in st.session_state:
    st.session_state.student_dictionary = {}

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

def add_student_callback():
    name = st.session_state.new_student_name.strip().title()
    if name:
        if name not in st.session_state.student_dictionary:
            st.session_state.student_dictionary[name] = {
                "average": {"score": 0, "grade": ""},
                "grade": []
            }
            st.success(f"Student {name} added successfully.")
        else:
            st.warning("Name already exists.")
    else:
        st.error("Student name cannot be empty.")
    st.session_state.new_student_name = "" # Clear input after submission

def add_grade_callback():
    student_name = st.session_state.grade_student_name.strip().title()
    grades_input = st.session_state.new_grades_input.strip()

    if student_name not in st.session_state.student_dictionary:
        st.error("Student not found.")
        return

    if not grades_input:
        st.error("Please enter grades.")
        return

    grades_list = []
    for g in grades_input.split(','):
        try:
            score = int(g.strip())
            if 0 <= score <= 100:
                grades_list.append(score)
            else:
                st.error(f"Invalid grade: {score}. Grades must be between 0 and 100.")
                return
        except ValueError:
            st.error(f"Invalid input: '{g.strip()}' is not a valid number. Please enter comma-separated numbers.")
            return
    
    st.session_state.student_dictionary[student_name]["grade"].extend(grades_list)
    grade_avg_calc(st.session_state.student_dictionary[student_name])
    st.success(f"{len(grades_list)} grades added successfully for {student_name}.")
    st.session_state.new_grades_input = "" # Clear input after submission

def view_report_callback():
    student_name = st.session_state.report_student_name.strip().title()
    if student_name in st.session_state.student_dictionary:
        student = st.session_state.student_dictionary[student_name]
        grade_avg_calc(student) # Ensure latest average is calculated
        st.subheader(f"Report for {student_name}")
        st.write(f"**Average Score:** {student['average']['score']} (Grade: {student['average']['grade']})")
        st.write(f"**Grades:** {', '.join(map(str, student['grade'])) if student['grade'] else 'No grades entered.'}")
    else:
        st.error("Student not found.")

st.title("Student Gradebook")

# Use tabs for navigation
tab1, tab2, tab3, tab4 = st.tabs(["Add Student", "Add Grade", "View Student Report", "Class Statistics"])

with tab1:
    st.header("Add New Student")
    with st.form("add_student_form"):
        st.text_input("Student Name", key="new_student_name")
        st.form_submit_button("Add Student", on_click=add_student_callback)

with tab2:
    st.header("Add Grades to Student")
    with st.form("add_grade_form"):
        st.selectbox("Select Student", options=[""] + list(st.session_state.student_dictionary.keys()), key="grade_student_name")
        st.text_area("Enter Grades (comma-separated, e.g., 85, 90, 78)", key="new_grades_input")
        st.form_submit_button("Add Grades", on_click=add_grade_callback)

with tab3:
    st.header("View Student Report")
    with st.form("view_report_form"):
        st.selectbox("Select Student", options=[""] + list(st.session_state.student_dictionary.keys()), key="report_student_name")
        st.form_submit_button("View Report", on_click=view_report_callback)

with tab4:
    st.header("Class Statistics")
    if not st.session_state.student_dictionary:
        st.info("No students in the gradebook yet.")
    else:
        total_class_score = 0
        num_students_with_grades = 0
        
        for name, student in st.session_state.student_dictionary.items():
            grade_avg_calc(student) # Ensure all averages are up-to-date
            if student["average"]["score"] != 0 or student["grade"]:
                total_class_score += student["average"]["score"]
                num_students_with_grades += 1

        if num_students_with_grades > 0:
            class_avg = total_class_score / num_students_with_grades
            st.subheader(f"Overall Class Average Score: {class_avg:.2f}")
        else:
            st.info("No grades entered for any student yet to calculate class average.")

        st.subheader("Individual Student Summaries:")
        for name, student in st.session_state.student_dictionary.items():
            grade_avg_calc(student) # Recalculate to be safe
            st.write(f"**Name:** {name}, **Average Score:** {student['average']['score']} (Grade: {student['average']['grade']}), **Grades:** {', '.join(map(str, student['grade'])) if student['grade'] else 'No grades entered.'}")