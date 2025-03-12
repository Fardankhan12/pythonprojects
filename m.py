import streamlit as st
import re 
st.title("Password Strength Manager by Mr. Fardan Khan")
def psm(password):
    prediction = 0
    mistakes = []
    if len(password) >= 8:
        prediction += 1
    else:
        mistakes.append("Password must be at least 8 characters")
    if re.search('[a-z]', password) and re.search('[A-Z]', password):
        prediction += 1
    else:
        mistakes.append("Password must contain at least one uppercase and one lowercase letter")
    if re.search(r'\d', password):
        prediction += 1
    else:
        mistakes.append("Password must contain at least one number")
    if re.search('[!@#$%^&*()_+-]', password):
        prediction += 1
    else:
        mistakes.append("Password must contain at least one special character")
    return prediction, mistakes

password = st.text_input("Enter your password:")
strength, mistakes = psm(password)
st.write("Password strength:", strength)
for mistake in mistakes:
    st.write(mistake)
if strength == 1:
    st.write("Weak **your password is 25% secured**")
elif strength == 2:
    st.write("Medium **your password is 50% secured**")
elif strength == 3:
    st.write("Very Strong **your password is 75% secured**")
elif strength == 4:
    st.write("Extremely Strong **your password is 100% secured**")
