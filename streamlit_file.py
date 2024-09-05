import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.header("Характеристики числовых столбцов", anchor=None)
df = pd.read_csv('D_client_data.csv')
df_stat = df.describe().T
st.table(df_stat)


st.header("Матрица корреляции признаков", anchor=None)
fig = plt.figure(figsize=(10, 4))
sns.heatmap(df.corr(), annot = True, vmin=-1, vmax=1, center= 0, cmap= 'coolwarm')
st.pyplot(fig)


fig = plt.figure()
sns.pairplot(df)
st.pyplot(fig)