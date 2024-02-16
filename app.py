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

option = st.radio('Select an option: ', ['Description','Display'])

if option == 'Description':
  st.write(data.description)

elif option == 'Display':
  first_intances = st.input_number('Number of first instances:', value=5)
  st.subheader("First %d instances:", %first_intances)
  st.write(data.head(first_intances))

  st.subheader("Last 5 instances:")
  st.write(data.tail())

  st.subheader("Random sample of instances:")
  st.write(data.sample(5))

