import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

widget_id = (id for id in range(1, 100_00))

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
  st.write('# Dimension of data set DTCR:')
  st.write('%d instances and %d features' %(data.shape[0], data.shape[1]))
  st.write('# Description of features or variables:')
  data_descriptions = {
        'Age': 'Age of patient (years)',
        'Gender': 'Gender of patient (F: Feminine, M: Masculine)',
        'Smoking': 'Current smoking status at the time of assessment (No, Yes)',
        'Hx Smoking': 'Medical history of smoking, that is, person\'s past smoking habits, regardless of their current smoking status (No, Yes)',
        'Hx Radiothreapy': 'Medical history of radiotherapy, that is, radiotherapy treatment in the past (No, Yes)',
        'Thyroid Function': 'Activity and hormone production (such as TSH, T3, and T4) of the thyroid gland (Euthyroid, Clinical Hyperthyroidism, Clinical Hypothyroidism, Subclinical Hyperthyroidism, Subclinical Hypothyroidism)',
        'Physical Examination': 'Examination of thyroid gland, assessing the size, shape, and texture, and evaluating for any nodules or abnormalities (Single nodular goiter - left, Multinodular goiter, Single nodular goiter - right, Normal, Diffuse goiter)',
        'Adenopathy': 'Enlargement or swelling of lymph nodes (No, Right, Extensive, Left, Bilateral, Posterior)',
        'Pathology': 'Types of carcinomas affecting the thyroid gland (Micropapillary, Papillary, Follicular, Hurthel cell)',
        'Focality': 'Number of distinct lesions or nodules present within the thyroid gland (Uni-Focal, Multi-Focal)',
        'Risk': 'The American Thyroid Association (ATA) risk score is a tool used to assess the risk of thyroid nodules for malignancy (Low, Intermediate, High)',
        'T': 'The T (Tumor) category describes the size and extent of the primary tumor within the thyroid gland (T1a, T1b, T2, T3a, T3b, T4a, T4b)',
        'N': 'The N (Lymph Nodes) category indicates whether there is involvement of regional lymph nodes near the thyroid gland (N0, N1a, N1b)',
        'M': 'The M (Metastasis) category indicates whether there is distant metastasis, meaning the spread of cancer cells from the thyroid gland to distant organs or tissues outside the neck region (M0, M1)',
        'Stage': 'Stages of thyroid cancer using TNM system (I, II, III, IVA, IVB)',
        'Response': 'Results of diagnostic tests or averall status of thyroid condition (Indeterminate, Excellent, Structural Incomplete, Biochemical Incomplete)',
        'Recurred': ' (Target variable) Reappearance or return of a thyroid condition after a period of remission or successful treatment (No, Yes)'
    }
  # https://www.ncbi.nlm.nih.gov/books/NBK65719.15/table/  
  
  for col in data.columns:
    st.write(f"{col}: {data_descriptions[col]}")
    
  st.write('# Type of features:')
  st.write("Numeric features:", data.select_dtypes('number').columns, "\n", "-"*100)
  st.write("Categorical features:", data.select_dtypes('object').columns)
  
  st.write('# Categorical features and factors:')
  for col in data.select_dtypes(include=object):
    st.write(f"The feature %s has %d factor(s): %s" %(col, data[col].nunique(), data[col].unique()))

elif option == 'EDA':
  st.write('# Exploratory data analysis (EDA)')
  st.write('# Numeric variable:')
  st.write(data.describe().T)
  
  if st.checkbox('Visualization'):
    binwidth=st.number_input('Binwidth of histogram:', value=5)
    plt.subplots()
    data['Age'].hist(bins=range(min(data['Age']), max(data['Age'])+binwidth, binwidth), color='blue')
    plt.title('Histogram of DTCR feature: Age')
    plt.xlabel('Age')
    st.pyplot(plt)

    plt.subplots()
    sns.boxplot(data['Age'])
    plt.title('Boxplot of DTCR feature: Age')
    plt.ylabel('Age')
    st.pyplot(plt)
  
  if st.checkbox('Age - Grouped data'):
    st.write(data.groupby('Recurred')['Age'].describe())

    binwidth_grouped=st.number_input('Binwidth of histogram:', value=5, key=next(widget_id))
    data_Age_No = data[data["Recurred"] == 'No']['Age']
    data_Age_Yes = data[data["Recurred"] == 'Yes']['Age']
    plt.subplots()
    data_Age_No.hist(bins=range(min(data_Age_No), max(data_Age_No) + binwidth_grouped, binwidth_grouped), color='blue', label='Recurred: No', alpha=0.6)
    data_Age_Yes.hist(bins=range(min(data_Age_Yes), max(data_Age_Yes) + binwidth_grouped, binwidth_grouped), color='red', label='Recurred: Yes', alpha=0.6)
    plt.legend()
    plt.title('Histogram of DTCR feature: Age\n Grouped by target feature: Recurred')
    plt.xlabel('Age')
    st.pyplot(plt)

    plt.subplots()
    plt.title('Boxplot of DTCR feature: Age\n Grouped by target feature: Recurred')
    sns.boxplot(y='Age',x='Recurred', data=data, palette=['blue','red'])
    plt.xlabel('Recurred')
    plt.ylabel('Age')
    st.pyplot(plt)

  st.write('# Categorical features:')
  st.write(data.describe(include = object).T)
  
  st.write('# Target feature:')
  f_abs = data["Recurred"].value_counts()
  f_rel = data["Recurred"].value_counts(normalize=True).round(4)
  f_rel_perc = (data["Recurred"].value_counts(normalize=True)*100).round(2)
  table = pd.concat([f_abs, f_rel, f_rel_perc], axis=1)
  table.columns = ["Absolute frequency", "Relative frequency", "Relative frequency (%)"]
  st.write(table)
  if st.checkbox('Visualization', key=next(widget_id)):
    plt.subplots()
    sns.countplot(x='Recurred', data=data, palette = "Set1")
    plt.title('Barplot of target feature')
    st.pyplot(plt)
