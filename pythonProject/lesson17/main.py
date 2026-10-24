import streamlit as st

st.header("BMI Calculator")

# Enter name
name = st.text_input("Enter name:")

# Enter age
age = st.number_input("Enter age:", min_value=1, max_value=120, value=18)

# Enter weight
weight = st.number_input("Enter weight in kilograms:", min_value=1.0, max_value=300.0, value=70.0)

# Enter height
height = st.number_input("Enter height in meters:", min_value=0.1, max_value=2.5, value=1.75)

# Store people
if "people" not in st.session_state:
    st.session_state.people = []

# Add person button
if st.button("Add person"):
    if name.strip():
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        person = {
            "Name": name,
            "Age": age,
            "Weight (kg)": weight,
            "Height (m)": height,
            "BMI": round(bmi, 2),
            "Category": category
        }

        st.session_state.people.append(person)

        st.success(f"{name} has been added!")

    else:
        st.error("Please enter a name.")

# Show results
st.header("Results")

if st.session_state.people:
    for person in st.session_state.people:
        st.subheader(person["Name"])

        st.write("Age:", person["Age"])
        st.write("Weight:", person["Weight (kg)"], "kg")
        st.write("Height:", person["Height (m)"], "m")
        st.write("BMI:", person["BMI"])
        st.write("Category:", person["Category"])

        st.divider()
else:
    st.info("No people have been added yet.")