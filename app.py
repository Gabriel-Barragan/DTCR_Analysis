import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

st.title('Differentiated Thyroid Cancer Recurrence Analysis')

st.header('Author: Gabriel Barragán')
st.subheader('E-mail: gbarragan@yachaytech.edu.ec')

data = pd.read_csv('Datasets/Thyroid_Diff.csv')
data.description = '''This data set contains 13 clinicopathologic features aiming to predict recurrence of well differentiated thyroid cancer.
The data set was collected in duration of 15 years and each patient was followed for at least 10 years.

Borzooei,Shiva and Tarokhian,Aidin. (2023). Differentiated Thyroid Cancer Recurrence. UCI Machine Learning Repository. https://doi.org/10.24432/C5632J.
'''

option = st.sidebar.radio('Select an option: ', ['Description','Display','Features','EDA'])

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
  st.write('# Features or variables:')
  for col in data.columns:
    st.write(col)
    
  st.write('Type of features:')
  st.write("Numeric features:", data.select_dtypes('number').columns, "\n", "-"*100)
  st.write("Categorical features:", data.select_dtypes('object').columns)
  
  st.write('Categorical features and factors:')
  for col in data.select_dtypes(include=object):
    st.write(f"The feature %s has %d factor(s): %s" %(col, data[col].nunique(), data[col].unique()))

elif option == 'EDA':
  st.write('# Exploratory data analysis (EDA)')
  st.write('# Numeric variable:')
  st.write(data.describe().T)
  if st.checkbox('Grouped data'):
    st.write(data.groupby('Recurred')['Age'].describe())

  st.write('# Categorical features:')
  st.write(data.describe(include = object).T)
  
  st.write('# Target feature:')
  f_abs = data["Recurred"].value_counts()
  f_rel = data["Recurred"].value_counts(normalize=True).round(4)
  f_rel_perc = (data["Recurred"].value_counts(normalize=True)*100).round(2).astype(str) + ' %'
  table = pd.concat([f_abs, f_rel, f_rel_perc], axis=1)
  table.columns = ["Absolute frequency", "Relative frequency", "Relative frequency (%)"]
  st.write(table)
