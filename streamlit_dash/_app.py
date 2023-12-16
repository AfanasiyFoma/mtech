import streamlit as st
import pandas as pd


st.title("Hello GeeksForGeeks !!!")


data1 = pd.read_csv('https://github.com/AfanasiyFoma/mtech/blob/main/streamlit_dash/file1.csv')

print(data1.head())
