import streamlit as st
from datetime import datetime

# Initialize budget_data in session_state if it doesn't exist
if 'budget_data' not in st.session_state:
    st.session_state.budget_data = {}

def format_currency(value):
    return f"${value:.2f}"

def add_entry_callback():
    entry_type = st.session_state.entry_type_select
    date_str = st.session_state.entry_date
    category = st.session_state.entry_category.strip().title()
    amount_str = st.session_state.entry_amount

    if not date_str or not category or not amount_str:
        st.error("All fields are required.")
        return

    try:
        datetime.strptime(date_str, "%Y-%m")
        amount = float(amount_str)
        if amount < 0:
            st.error("Amount cannot be negative.")
            return

        if date_str not in st.session_state.budget_data:
            st.session_state.budget_data[date_str] = {"income": {}, "expenses": {}}
        
        section = "income" if entry_type == "income" else "expenses"
        
        if category in st.session_state.budget_data[date_str][section]:
            st.session_state.budget_data[date_str][section][category] += amount
        else:
            st.session_state.budget_data[date_str][section][category] = amount
        
        st.success("Entry added successfully.")
        st.session_state.entry_date = ""
        st.session_state.entry_category = ""
        st.session_state.entry_amount = ""

    except ValueError:
        st.error("Invalid date format (use YYYY-MM) or amount (enter a number).")

st.title("Personal Budget Tracker")

# Use tabs for navigation
tab1, tab2 = st.tabs(["Add Entry", "View Monthly Summary"])

with tab1:
    st.header("Add New Entry")
    with st.form("add_entry_form"):
        st.radio("Type", ["income", "expense"], key="entry_type_select", horizontal=True)
        st.text_input("Date (YYYY-MM)", placeholder="e.g., 2025-08", key="entry_date")
        st.text_input("Category", key="entry_category")
        st.text_input("Amount", key="entry_amount")
        st.form_submit_button("Add Entry", on_click=add_entry_callback)

with tab2:
    st.header("View Monthly Summary")
    month_to_view = st.selectbox("Select Month (YYYY-MM)", options=[""] + sorted(list(st.session_state.budget_data.keys()), reverse=True), key="month_view_select")

    if month_to_view:
        if month_to_view not in st.session_state.budget_data:
            st.info("No data for this month.")
        else:
            data = st.session_state.budget_data[month_to_view]
            income = data.get("income", {})
            expenses = data.get("expenses", {})

            total_income = sum(income.values())
            total_expenses = sum(expenses.values())
            net = total_income - total_expenses

            st.subheader(f"Summary for {datetime.strptime(month_to_view, '%Y-%m').strftime('%B %Y')}")
            st.markdown("---")
            st.metric(label="Total Income", value=format_currency(total_income))
            st.metric(label="Total Expenses", value=format_currency(total_expenses))
            st.metric(label="Net Savings", value=format_currency(net), delta=f"{(net/total_income*100 if total_income else 0):.1f}%" if total_income else None)
            st.markdown("---")

            st.subheader("Expense Breakdown")
            if expenses:
                for category, amount in expenses.items():
                    percentage = amount / total_expenses * 100 if total_expenses else 0
                    st.write(f"**{category}**: {format_currency(amount)} ({percentage:.1f}%) ")
                    st.progress(int(percentage))
            else:
                st.info("No expenses recorded for this month.")
    else:
        st.info("Select a month to view its summary.")
