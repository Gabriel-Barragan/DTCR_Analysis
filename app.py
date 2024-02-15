import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
import streamlit as st

st.title('Hello world!')

st.header('header')
st.text('text2')

st_name = st.sidebar.text_input('Enter your name: ','Gabriel')

st.write('Hello', st_name, '!')
