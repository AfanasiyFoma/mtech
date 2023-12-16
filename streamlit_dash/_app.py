import streamlit as st
import pandas as pd


st.title("Hello World !!!")


df = pd.read_csv('https://github.com/AfanasiyFoma/mtech/blob/main/streamlit_dash/file1.csv')

print(df.head())

st.bar_chart(data=df.groupby('Пол')['Возраст'], x='Пол', y='Возраст', use_container_width=True)
