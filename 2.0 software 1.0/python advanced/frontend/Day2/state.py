import streamlit as st

if "count" not in st.session_state:
    st.session_state.count = 0
if st.button("Increment"):
    st.session_state.count += 1
st.write(f"Count: {st.session_state.count}")
    

        
            
# count = 0

# if st.button("Increment"):
#     count += 1

# st.write(f"Count: {count}")