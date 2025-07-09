import streamlit as st
st.title("Multi Widget Demo App")
name=st.text_input("Enter your name:")
number=st.select_slider("Select a number:", options=list(range(3,12)),value=9)
color=st.radio("Pick your favourite color:",["Red","Black","Blue"])
subscribe=st.checkbox("Subscribe to my channel")
age=st.number_input("Enter your age:",min_value=0)
if st.button("Submit"):
    st.write(f"Hello {name}!")
    st.write(f"You selected {number}")
    st.write(f"Your favorite color is {color}")
    st.write(f"Subscription status: {'Subscribed' if subscribe else 'Not Subscribed'}")
    st.write(f"Your age is {age}")
