import streamlit as st

# st.title("Hello bod")

# st.write("Sharp sentinel")
# st.header("Uptymos Prrr")

# st.write({
#     "the way": "up",
#     "phone num": 3.14,
#     "ip": 1,
#     "added": 3*5
# })

# ## STREAMLIT FLOW
# print("run")
# pressed = st.button("Stangle")

# print(pressed)

from profile import markdown_code

st.title("WELCOME")
st.header("WELCOME")
st.subheader("WELCOME")
st.image("C:/Users/atsim/Videos/Captures/Screenshot 7_6_2025 6_07_22 PM.png", caption="Welcome to the app", use_column_width=True)

uploaded_image = st.file_uploader("Upload an image", type=["png","jpeg","jpg"])

if uploaded_image:
    st.image(uploaded_image, caption = "Uploaded image!", use_column_width=True)

st.markdown(markdown_code)