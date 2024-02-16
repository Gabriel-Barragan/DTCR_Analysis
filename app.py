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

option = st.radio('Seleccione una opción: ', ['Descripción'])

if option == 'Descripción':
  st.write(data.description)

