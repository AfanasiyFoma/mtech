import streamlit as st
import pandas as pd
import plost


st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.sidebar.header('Dashboard `Mtech`')

st.sidebar.subheader('Heat map parameter')
time_hist_color = st.sidebar.selectbox('Color by', ('М', 'Ж')) 
data1 = pd.read_csv('https://github.com/AfanasiyFoma/mtech/blob/main/streamlit_dash/file1.csv')
link for requirements.txt
https://github.com/AfanasiyFoma/mtech/blob/main/streamlit_dash/requirements.txt

                   
st.markdown('### Распредение по полу')
st.bar_chart(data=data1, x='Дни болезни', y='Количество случаев', use_container_width=True)
