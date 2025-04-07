import streamlit as st

st.title("BMI Calculator")
weight = st.number_input("Enter your weight (kg)")
height = st.number_input("Enter your height (m)")

if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.write(f"Your BMI is: {bmi:.2f}")
    else:
        st.write("Height must be greater than zero.")