
import streamlit as st
import pandas as pd
import plost

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.sidebar.header('Dashboard `Mtech`')

st.sidebar.subheader('Heat map parameter')
time_hist_color = st.sidebar.selectbox('Color by', ('М', 'Ж')) 



st.sidebar.subheader('Line chart parameters')
plot_data = st.sidebar.multiselect('Select data', ['temp_min', 'temp_max'], ['temp_min', 'temp_max'])


st.sidebar.markdown('''
---
''')




# Row B
data = pd.read_csv('https://github.com/AfanasiyFoma/mtech/blob/main/streamlit_dash/file1.csv)

c1, c2 = st.columns((7,3))
with c1:
    st.markdown('### Распредение по полу')
    plost.time_hist(
    data=data,
    date='date',
    x_unit='Пол',
    y_unit='Количество в категории',
    color=time_hist_color,
    aggregate='median',
    legend=None,
    height=345,
    use_container_width=True)
with c2:
    st.bar_chart(data=seattle_weather, *, x='Дни болезни', y='Количество случаев', use_container_width=True)
    x1 = list(data[data['Пол'] == 'М']['Количество больничных дней'])
    x2 = list(data[data['Пол'] == 'Ж']['Количество больничных дней'])


plt.hist([x1, x2], bins = 9, color = colors)



# Row C
st.markdown('### Line chart')
st.line_chart(data, x = 'date', y = plot_data, height = plot_height)
