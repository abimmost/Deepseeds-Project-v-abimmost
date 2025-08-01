# === PERSONAL BUDGET TRACKER ===
# Review and comment my code which will be studied by a beginner python programmer

from datetime import datetime

budget_data = {}

# Function to format currency
def format_currency(value):
    return f"${value:.2f}"

# Function to add income or expense
def add_entry():
    try:
        entry_type = input("Type (income/expense): ").lower()
        if entry_type not in ["income", "expense"]:
            print("Invalid type.")
            return
        date = input("Enter date (YYYY-MM): ")
        datetime.strptime(date, "%Y-%m")  # Validate date
        category = input("Enter category: ").title()
        amount = float(input("Enter amount: "))
        if date not in budget_data:
            budget_data[date] = {"income": {}, "expenses": {}}
        section = "income" if entry_type == "income" else "expenses"
        if category in budget_data[date][section]:
            budget_data[date][section][category] += amount
        else:
            budget_data[date][section][category] = amount
        print("Entry added successfully.")
    except ValueError:
        print("Invalid input or date.")

# Function to view monthly summary
def view_summary():
    date = input("Enter month to view (YYYY-MM): ")
    if date not in budget_data:
        print("No data for this month.")
        return

    income = budget_data[date].get("income", {})
    expenses = budget_data[date].get("expenses", {})

    total_income = sum(income.values())
    total_expenses = sum(expenses.values())
    net = total_income - total_expenses

    print(f"\n=== PERSONAL BUDGET TRACKER ===\nMonth: {datetime.strptime(date, '%Y-%m').strftime('%B %Y')}\n")
    print("💰 FINANCIAL SUMMARY")
    print(f"Total Income: {format_currency(total_income)}")
    print(f"Total Expenses: {format_currency(total_expenses)}")
    print(f"Net Savings: {format_currency(net)} ({(net/total_income*100 if total_income else 0):.1f}%)\n")

    print("📊 EXPENSE BREAKDOWN")
    for category, amount in expenses.items():
        percentage = amount / total_expenses * 100 if total_expenses else 0
        bar = "█" * int(percentage // 2) + "░" * (20 - int(percentage // 2))
        print(f"{category:<12} {bar} {format_currency(amount)} ({percentage:.1f}%)")

# === MAIN LOOP ===
while True:
    print("\n1. Add Entry\n2. View Monthly Summary\n3. Exit")
    try:
        choice = int(input("Choose option: "))
        if choice == 1:
            add_entry()
        elif choice == 2:
            view_summary()
        elif choice == 3:
            print("Exiting program.")
            break
        else:
            print("Invalid option.")
    except ValueError:
        print("Enter a valid number.")
