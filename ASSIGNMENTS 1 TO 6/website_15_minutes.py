import streamlit as st

st.set_page_config(page_title="My Python Website", page_icon="🌍")

st.title("Welcome to My Python Website")

st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

if page == "Home":
    st.header("Home Page")
    st.write("This is a simple website built with Streamlit.")


    st.image("assests/main.jpg", caption="Local Image", use_column_width=True)

elif page == "About":
    st.header("About")
    st.write("This website was created using Python and Streamlit.")

elif page == "Contact":
    st.header("Contact")
    name = st.text_input("Enter your name")
    email = st.text_input("Enter your email")
    message = st.text_area("Enter your message")

    if st.button("Submit"):
        st.success(f"Thank you, {name}! We'll get back to you at {email}.")
