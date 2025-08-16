import streamlit as st

def check_password_strength(password):
    feedback = []
    is_valid = True

    if len(password) < 8:
        feedback.append("Password must be at least 8 characters long.")
        is_valid = False

    upper = False
    lower = False
    digit = False
    special = False

    for char in password:
        if char.isupper():
            upper = True
        elif char.islower():
            lower = True
        elif char.isdigit():
            digit = True
        elif char in "!@#$%^&*":
            special = True

    if not upper:
        feedback.append("Password must contain at least one uppercase letter.")
        is_valid = False
    if not lower:
        feedback.append("Password must contain at least one lowercase letter.")
        is_valid = False
    if not digit:
        feedback.append("Password must contain at least one digit.")
        is_valid = False
    if not special:
        feedback.append("Password must contain at least one special character: !@#$%^&*")
        is_valid = False

    return is_valid, feedback

def analyze_password_callback():
    password = st.session_state.password_input
    if password:
        is_valid, feedback = check_password_strength(password)
        if is_valid:
            st.success("Password is valid!")
        else:
            st.error("Password is not valid. Please address the following issues:")
            for item in feedback:
                st.warning(f"- {item}")
    else:
        st.info("Please enter a password to analyze.")

st.title("Password Analyzer")

st.markdown("**Password Requirements:**")
st.markdown("- 8 characters long")
st.markdown("- At least one uppercase letter")
st.markdown("- At least one lowercase letter")
st.markdown("- At least one digit")
st.markdown("- At least one special character: `!@#$%^&*`")

with st.form("password_form"):
    st.text_input("Enter your password:", type="password", key="password_input")
    st.form_submit_button("Analyze Password", on_click=analyze_password_callback)
