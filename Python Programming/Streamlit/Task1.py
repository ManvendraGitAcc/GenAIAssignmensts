import streamlit as st
st.title("Welcome to StreamLit!")
input = st.text_input("Enter your name")
if st.button("Greet Me"):
    st.write(f"Hello, {input}!")
