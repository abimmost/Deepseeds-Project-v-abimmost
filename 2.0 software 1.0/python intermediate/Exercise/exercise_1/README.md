# Solution

This program is a simple student gradebook system. It allows users to add students, record their grades, view individual student reports, and display class statistics including the class average. The program uses a dictionary to store student data, including their grades and calculated averages.

# Approach

The solution uses several Python constructs:

- **Dictionary**: Stores all student records and their grades.
- **Functions**: Each operation (add student, add grades, calculate averages, display reports) is handled by a separate function for clarity and reuse..
- **Loops**: `while` loops are used for menu navigation and for entering multiple grades.
- **Conditional statements**: `if`, `elif`, and `else` are used to check user choices, validate input, and assign letter grades.
- **String methods**: `.title()` is used to format student names.
- **Exception handling**: `try` and `except` blocks ensure robust input validation.
- **List operations**: Grades are stored in lists and processed using `sum()` and `len()` for average calculations.

This structure makes the program easy to understand and extend for beginner Python programmers.
