import streamlit as st
productDB = {"Product":[], "Category":[], "Price": []}
st.title("Welcome to StreamLit!",width= "content")

product = st.sidebar.text_input("Product Name")
option = st.sidebar.selectbox("Category" , ("Mobile", "Monitor", "Mouse", "Keyboard"))
price = st.sidebar.number_input("Price")
if st.sidebar.button("Add Product"):
    productDB["Product"].append(product)
    productDB["Category"].append(option)
    productDB["Price"].append(price)
    st.write("Product added successfully ")
    st.table(productDB, border=True)

