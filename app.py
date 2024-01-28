
import streamlit as st

st.title('Hello world!')

st.header('header')
st.text('text2')

st_name = st.sidebar.text_input('Enter your name: ','Gabriel')

#st.write(f'Hello {st_name}!')
st.write('Hello', st_name, '!')
