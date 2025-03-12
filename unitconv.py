import streamlit as st
st.title("Unit Converter By Mr. Fardan Khan")
def converter():
    value = st.number_input("Enter the value")
    option = st.selectbox("Select the unit you want to convert", ["Kilometers to Miles", "Miles to Kilometers", "Celsius to Fahrenheit", "Fahrenheit to Celsius", "Kilograms to Pounds", "Pounds to Kilograms"])
    if option == "Kilometers to Miles":
        result = value * 0.621371
        st.write(f"**Conversion formula** = {value}   *   0.621371")
        st.write(result, "miles")
    elif option == "Miles to Kilometers":
        result = value * 1.60934
        st.write(f"**Conversion formula** = {value}  *  1.60934 ")
        st.write(result, "kilometers")
    elif option == "Celsius to Fahrenheit":
        result = (value * 9/5) + 32
        st.write(f"**Conversion formula** = {value}  *  9/5 + 32")
        st.write(result, "Fahrenheit")
    elif option == "Fahrenheit to Celsius":
        result = (value - 32) * 5/9
        st.write(f"**Conversion formula** = ({value} - 32)  *  5/9")
        st.write(result, "Celsius")
    elif option == "Kilograms to Pounds":
        result = value * 2.20462
        st.write(f"**Conversion formula** = {value}  *  2.20462")
        st.write(result, "pounds")
    elif option == "Pounds to Kilograms":
        result = value * 0.453592
        st.write(f"**Conversion formula** = {value}  *  0.453")
        st.write(result, "kilograms")
converter()