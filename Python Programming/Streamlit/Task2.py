import streamlit as st

st.title("Welcome to StreamLit!",width= "content")
input = st.text_input("Product Price ")
disc = st.slider("Discount Percentage", min_value = 0, max_value = 50)
if st.button("Calculate"):    
    st.success(f"{float(input) - (float(input)*disc)/100}")
    st.title(":blue[Comparison]", text_alignment="center", width = "content")
    st.table({"Price":[input],"Discount":[disc],"Price After Discount":[ disc]},border="horizontal")
