import streamlit as st

st.title("My app")

name = st.text_input("What is your name?")
age = st.slider("Your age", 10, 60, 20)

if st.button("Say hello"):
    st.success(f"Hello {name}, you are {age}!")
st.write("your name has",len(name),"letters")