import streamlit as st

st.set_page_config(page_title="Unit Converter App", page_icon="🌍")

st.title("🌍 Unit Converter App")

st.markdown("## Convert between different units")
st.write("This app converts between different units of **Length**, **Mass**, and **Temperature**.")

# Category selection
category = st.selectbox(
    "Select the category of units you want to convert:",
    ["Length", "Mass", "Temperature"]
)

# Unit options based on category
if category == "Length":
    unit = st.selectbox(
        "Select the conversion type:",
        ["Meters to Feet", "Feet to Meters", "Miles to Kilometers", "Kilometers to Miles"]
    )
elif category == "Mass":
    unit = st.selectbox(
        "Select the conversion type:",
        ["Kilograms to Pounds", "Pounds to Kilograms"]
    )
elif category == "Temperature":
    unit = st.selectbox(
        "Select the conversion type:",
        ["Celsius to Fahrenheit", "Fahrenheit to Celsius", "Celsius to Kelvin", "Kelvin to Celsius"]
    )

# Input value
value = st.number_input("Enter the value you want to convert:", format="%.4f")

# Conversion function
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Meters to Feet":
            return value * 3.28084
        elif unit == "Feet to Meters":
            return value / 3.28084
        elif unit == "Miles to Kilometers":
            return value * 1.60934
        elif unit == "Kilometers to Miles":
            return value / 1.60934

    elif category == "Mass":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462

    elif category == "Temperature":
        if unit == "Celsius to Fahrenheit":
            return value * 9 / 5 + 32
        elif unit == "Fahrenheit to Celsius":
            return (value - 32) * 5 / 9
        elif unit == "Celsius to Kelvin":
            return value + 273.15
        elif unit == "Kelvin to Celsius":
            return value - 273.15

    return None  # Fallback in case of an unexpected input

# Convert button
if st.button("Convert"):
    result = convert_units(category, value, unit)

    if result is not None:
        st.success(f"The converted {category.lower()} is **{result:.2f}**.")
    else:
        st.error("Conversion failed. Please check your input or unit selection.")

# Optional: Reset button
if st.button("Reset"):
    st.rerun()
