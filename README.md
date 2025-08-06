

# 🐍 Python Challenge Arena
*A 2-hour coding adventure to test your Python skills*

## 📋 Overview
Complete 5 progressively challenging exercises that test your knowledge of variables, lists, conditionals, loops, functions, and dictionaries. Each exercise requires creating a well-formatted command-line interface and solving real-world problems.

## 🎯 Learning Objectives
- Apply Python fundamentals in practical scenarios
- Create user-friendly command-line interfaces
- Practice problem-solving and algorithmic thinking
- Write clean, readable code

## 📁 Repository Structure
```
python-challenge-arena/
├── README.md
├── exercise_1/
│   ├── student_gradebook.py
│   └── README.md
├── exercise_2/
│   ├── inventory_manager.py
│   └── README.md
├── exercise_3/
│   ├── password_analyzer.py
│   └── README.md
├── exercise_4/
│   ├── quiz_master.py
│   └── README.md
└── exercise_5/
    ├── budget_tracker.py
    └── README.md
```


---

## 🏆 Exercise 1: Student Gradebook Manager
**Points: 15** | **Time: 20 minutes**

### 📂 Setup
Create folder `exercise_1/` with file `student_gradebook.py`

### 🎯 Challenge
Build a gradebook that calculates student averages and determines letter grades.

### 📋 Requirements
1. Store student data in a dictionary format: `{"name": [list_of_grades]}`
2. Create a menu system with options:
   - Add new student
   - Add grade to existing student
   - View student average and letter grade
   - Display class statistics
   - Exit
3. Calculate letter grades: A(90+), B(80-89), C(70-79), D(60-69), F(<60)
4. Show class average and highest/lowest performing student

### 💡 Key Concepts Tested
- Dictionaries, lists, functions, loops, conditionals
- Menu-driven programming
- Statistical calculations

### ✅ Sample Output
```
=== STUDENT GRADEBOOK MANAGER ===
1. Add Student
2. Add Grade
3. View Student Report
4. Class Statistics
5. Exit
Choice: 3

Enter student name: Alice
Alice's Average: 87.5 (Grade: B)
Grades: [85, 92, 84, 89]
```

---

## 🏆 Exercise 2: Smart Inventory Manager
**Points: 20** | **Time: 25 minutes**

### 📂 Setup
Create folder `exercise_2/` with file `inventory_manager.py`

### 🎯 Challenge
Manage a store inventory with stock tracking and low-stock alerts.

### 📋 Requirements
1. Use nested dictionary: `{"item_name": {"price": float, "stock": int, "category": str}}`
2. Menu options:
   - Add new item
   - Update stock (add/remove)
   - Search items by category
   - Check low stock items (≤5 units)
   - Calculate total inventory value
   - Exit
3. Format currency properly ($XX.XX)
4. Handle invalid inputs gracefully

### 💡 Key Concepts Tested
- Nested dictionaries, string formatting
- Input validation, mathematical operations
- Filtering and searching algorithms

### ✅ Sample Output
```
=== SMART INVENTORY MANAGER ===
Current Inventory Value: $2,847.50

⚠️ LOW STOCK ALERT:
- Laptop (2 units remaining)
- Mouse (3 units remaining)

Choose option: 3
Category to search: Electronics
Found 4 items in Electronics:
• Laptop - $999.99 (2 in stock)
• Phone - $599.99 (15 in stock)
```

---

## 🏆 Exercise 3: Password Security Analyzer
**Points: 25** | **Time: 30 minutes**

### 📂 Setup
Create folder `exercise_3/` with file `password_analyzer.py`

### 🎯 Challenge
Analyze password strength and suggest improvements using multiple criteria.

### 📋 Requirements
1. Check passwords against these criteria:
   - Length (minimum 8 characters)
   - Contains uppercase letters
   - Contains lowercase letters
   - Contains numbers
   - Contains special characters (!@#$%^&*)
   - Not a common password (maintain list of 20+ common passwords)
2. Scoring system: Each criterion = 20 points (max 120 points)
3. Strength levels: Weak(0-40), Fair(41-60), Good(61-80), Strong(81-100), Excellent(101-120)
4. Generate specific improvement suggestions

### 💡 Key Concepts Tested
- String methods, character validation
- List membership, scoring algorithms
- Complex conditional logic

### ✅ Sample Output
```
=== PASSWORD SECURITY ANALYZER ===
Enter password to analyze: MyP@ss123

🔒 SECURITY ANALYSIS RESULTS
Password: MyP@ss123
Score: 100/120 (Strong)

✅ Length requirement (8+ chars)
✅ Contains uppercase letters  
✅ Contains lowercase letters
✅ Contains numbers
✅ Contains special characters
❌ Common password detected

💡 SUGGESTIONS:
- Avoid common password patterns
- Consider using a passphrase instead
```

---

## 🏆 Exercise 4: Interactive Quiz Master
**Points: 30** | **Time: 35 minutes**

### 📂 Setup
Create folder `exercise_4/` with file `quiz_master.py`

### 🎯 Challenge
Create a quiz system with multiple categories and difficulty tracking.

### 📋 Requirements
1. Store questions in nested dictionary:
   ```python
   {
     "category": {
       "easy": [{"question": "Q?", "options": ["A","B","C","D"], "answer": 0}],
       "hard": [...]
     }
   }
   ```
2. Features needed:
   - Choose category and difficulty
   - Track score and time per question
   - Show progress bar during quiz
   - Detailed results with correct answers for wrong questions
   - Save high scores to continue between runs
3. Include at least 3 categories with 5 questions each (easy/hard)

### 💡 Key Concepts Tested
- Complex nested data structures
- Time tracking, progress visualization
- File handling (bonus), advanced formatting

### ✅ Sample Output
```
=== QUIZ MASTER ===
Categories: Science, History, Sports

Selected: Science (Hard)
Question 2/5: What is the atomic number of Carbon?
[████████░░] 40% Complete

A) 4    B) 6    C) 8    D) 12
Your answer: B

✅ Correct! (+10 points)
Time: 3.2 seconds

FINAL SCORE: 80/100 (4/5 correct)
New personal best in Science!
```

---

## 🏆 Exercise 5: Personal Budget Tracker
**Points: 35** | **Time: 30 minutes**

### 📂 Setup
Create folder `exercise_5/` with file `budget_tracker.py`

### 🎯 Challenge
Build a comprehensive budget tracking system with analytics.

### 📋 Requirements
1. Track income and expenses by category and date
2. Data structure: `{"2024-01": {"income": {"salary": 3000}, "expenses": {"food": 400}}}`
3. Advanced features:
   - Monthly budget limits per category
   - Spending trend analysis (increasing/decreasing)
   - Budget variance warnings
   - Visual spending breakdown (text-based charts)
   - Export monthly summary
4. Handle date validation and formatting

### 💡 Key Concepts Tested
- Complex data manipulation, date handling
- Mathematical analysis, percentage calculations
- Advanced string formatting, data visualization

### ✅ Sample Output
```
=== PERSONAL BUDGET TRACKER ===
Month: January 2024

💰 FINANCIAL SUMMARY
Total Income: $3,200.00
Total Expenses: $2,150.00
Net Savings: $1,050.00 (32.8%)

📊 EXPENSE BREAKDOWN
Food        ████████████░░░░░░░░ $430 (20.0%)
Transport   ████████░░░░░░░░░░░░ $200 (9.3%)
Housing     ████████████████████ $800 (37.2%)

⚠️ BUDGET ALERTS:
Food: $30 over budget (107% of limit)
```

---

## 🎯 Scoring System

| Exercise | Points | Difficulty | Key Skills |
|----------|--------|------------|------------|
| Exercise 1 | 15 | ⭐⭐ | Dictionaries, Basic Functions |
| Exercise 2 | 20 | ⭐⭐⭐ | Nested Data, Input Validation |
| Exercise 3 | 25 | ⭐⭐⭐ | String Processing, Logic |
| Exercise 4 | 30 | ⭐⭐⭐⭐ | Complex Data Structures |
| Exercise 5 | 35 | ⭐⭐⭐⭐⭐ | Data Analysis, Advanced Features |

**Total Points: 125**

## 🏅 Achievement Levels
- **🥉 Bronze**: 60-79 points - "Python Apprentice"
- **🥈 Silver**: 80-99 points - "Code Craftsperson"  
- **🥇 Gold**: 100-119 points - "Python Professional"
- **💎 Platinum**: 120-125 points - "Code Master"

## 📝 Submission Guidelines

1. **File Structure**: Follow the exact folder/file naming
2. **Code Quality**: Include comments explaining complex logic
3. **User Experience**: Ensure clean, formatted output
4. **Error Handling**: Program shouldn't crash on invalid input
5. **Testing**: Test all menu options and edge cases

## 🚫 Academic Integrity
These exercises are designed to be AI-resistant through:
- Specific formatting requirements
- Integration of multiple concepts
- Real-world problem contexts
- Custom output formatting needs

Use these challenges to genuinely test and improve your Python skills!

---

**Good luck, and may your code be bug-free! 🐛✨**

This repository structure creates exercises that are:
- **AI-resistant**: Require specific formatting, integration of multiple concepts, and real-world problem-solving
- **Progressive difficulty**: Each exercise builds on previous knowledge
- **Practical**: Real-world applications students can relate to
- **Interface-focused**: Emphasis on clean, user-friendly command-line interfaces
- **Time-appropriate**: Designed for 2-hour completion with varying skill levels
- **Engaging**: Gamified with points and achievement levels

The exercises test all the concepts you mentioned while requiring students to think critically about user experience and code organization.
