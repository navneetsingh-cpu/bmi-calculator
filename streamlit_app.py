import streamlit as st


def calculate_bmi(weight, height):
    return weight / (height**2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"


st.title("BMI Calculator")

weight = st.number_input("Enter your weight (in kg)", min_value=1.0, max_value=300.0)
height = st.number_input("Enter your height (in m)", min_value=0.1, max_value=3.0)

if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)
    st.write(f"Your BMI is {bmi:.2f}, which is considered {category}.")

    if category == "Underweight":
        st.write(
            "You're underweight. It's important to eat a balanced and nutrient-rich diet. Consider consulting with a healthcare professional for advice."
        )
    elif category == "Normal weight":
        st.write(
            "You're within the normal weight range. Maintain a healthy lifestyle and balanced diet to stay in shape."
        )
    elif category == "Overweight":
        st.write(
            "You're overweight. Regular exercise and a healthy diet can help lose weight. Consider consulting with a healthcare professional for advice."
        )
    else:
        st.write(
            "You're in the obesity range. It's important to seek medical help to better understand your health situation."
        )
