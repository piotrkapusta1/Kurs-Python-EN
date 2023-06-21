import streamlit as st

st.header("Contact Me")

with st.form(key="my_forms"):
    user_email = st.text_input("Your email addresss")
    message = st.text_area("Your messange")
    button = st.form_submit_button()
    if button:
        message = message + user_email
        print("I was pressed!")