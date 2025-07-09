import streamlit as st
import pandas as pd
data={"Name":["Rohan","Shyam","Aman","Ravi"],"Age":[18,20,11,15],"Marks":[90,80,70,60]}
df=pd.DataFrame(data)
st.write("Simple Data Frame")
st.table(df)
st.write("Scrolling Data Frame")
st.dataframe(df)
