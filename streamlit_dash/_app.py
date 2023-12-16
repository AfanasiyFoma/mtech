import streamlit as st
import pandas as pd


st.title("Hello GeeksForGeeks !!!")


data1 = pd.read_csv('C:/openData/Mtech/2/file1.csv')

print(data1.head())

st.bar_chart(data=data1.groupby('Пол')['Возраст'], x='Пол', y='Возраст', use_container_width=True)
