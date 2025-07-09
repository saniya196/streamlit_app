import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(page_title="Student Marks Visualiser",page_icon="🧑‍🎓",layout="wide")
st.title("Student Marks Visualiser with charts")
method=st.radio("Choose Data Input:",["Upload CSV","Manual Input"])
if method=="Upload CSV":
    uploaded_file=st.file_uploader("Upload CSV file",type=["csv"])
    if uploaded_file is not None:
        df=pd.read_csv(uploaded_file)
        st.write("Uploaded Data:")
        st.dataframe(df)
elif method=="Manual Input":
    st.write("Enyter student Data:")
    num_students=st.number_input("Number of students:",min_value=1,max_value=100,value=5)
    names=[]
    marks=[]
    for i in range(num_students):
        name=st.text_input(f"Enter name of student {i+1}:")
        mark=st.number_input(f"Enter marks of student {i+1}:",min_value=0,max_value=100,value=0)
        names.append(name)
        marks.append(mark)
    if st.button("Submit"):
        df=pd.DataFrame({"Name": names, "Marks": marks})
        st.write("Entered Data:")
        st.dataframe(df)
if 'df' in locals() and not df.empty:
    st.write("Marks Bar Chart:")
    st.bar_chart(df.set_index("Name")["Marks"])
    average_marks = df['Marks'].mean()
    st.write(f"### 📊 Average Marks: {average_marks:.2f}")
    highest_marks=df['Marks'].max()
    topper=df[df['Marks']==highest_marks]
    name=topper['Name'].values[0]
    st.write(f"### 🥇 Topper is :",name,"with marks:",highest_marks)


    



