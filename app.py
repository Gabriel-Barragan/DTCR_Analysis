import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

st.title('Differentiated Thyroid Cancer Recurrence Analysis')

st.header('Autor: Gabriel Barragán')

data = pd.read_csv('Datasets/Thyroid_Diff.csv')
data.description = '''This data set contains 13 clinicopathologic features aiming to predict recurrence of well differentiated thyroid cancer.
The data set was collected in duration of 15 years and each patient was followed for at least 10 years.'''

option = st.radio('Select an option: ', ['Description','Display','Features'])

if option == 'Description':
  st.write(data.description)

elif option == 'Display':
  number_first_intances = st.number_input('Number of first instances:', value=5)
  st.subheader(f"First {number_first_intances} instances:")
  st.write(data.head(number_first_intances))

  number_last_intances = st.number_input('Number of last instances:', value=5)
  st.subheader(f"Last {number_last_intances} instances:")
  st.write(data.tail(number_last_intances))

  number_sample_intances = st.number_input('Number of random sample instances:', value=5)
  st.subheader(f"{number_sample_intances} Random sample of instances:")
  st.write(data.sample(number_sample_intances))

elif option == 'Features':
  st.write('Dimension of data set DTCR: %d instances and %d features' %(data.shape[0], data.shape[1]))
  st.write('Features or variables:')
  for col in data.columns:
    st.write(col)
