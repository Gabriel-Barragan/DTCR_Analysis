
import streamlit as st

st.title('Hello world!')

st.header('header')
st.text('text2')

st_name = st.text_input('Enter your name: ','Gabriel')

st.write(f'Hello {st_name}!')
