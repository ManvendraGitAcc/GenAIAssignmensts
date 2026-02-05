import streamlit as st
productDB = {"January" : 1200, "February":  1500, "March" : 900, "April" : 200}

st.title("Simple Sales Dashboard",width= "content")

def printSale(Sales : str):
    #st.write(productDB[Sales])
    st.metric(label = "Sale Price", value = productDB[Sales])
    st.bar_chart(list(productDB.values()),x_label="Month", y_label="Sale")


option = st.selectbox("Month",("January", "February", "March", "April"))
if st.button("Sales Report"):
    printSale(option)
