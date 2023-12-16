import streamlit as st
import pandas as pd
import plost


st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.sidebar.header('Dashboard `Mtech`')

st.sidebar.subheader('Heat map parameter')
time_hist_color = st.sidebar.selectbox('Color by', ('М', 'Ж')) 
data = pd.read_csv('https://github.com/AfanasiyFoma/mtech/blob/main/streamlit_dash/file1.csv')

                   
st.markdown('### Распредение по полу')
st.bar_chart(data=seattle_weather, *, x='Дни болезни', y='Количество случаев', use_container_width=True)
