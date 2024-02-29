#!/usr/bin/env python
# coding: utf-8

# ## DASHBOARD 

# In[1]:


# In[2]:


import streamlit as st
import pandas as pd
import plotly.express as px

# Memuat data dari file CSV
bike_data = pd.read_csv('bike_data_bersih.csv')

# Menghitung rata-rata penggunaan sepeda per hari dan per minggu
average_daily_users = bike_data['cnt'].mean()
average_weekly_users = average_daily_users * 7

# Menghitung rata-rata penggunaan sepeda pada hari kerja dan hari libur
average_usage_workday = bike_data[bike_data['workingday'] == 1]['cnt'].mean()
average_usage_holiday = bike_data[bike_data['workingday'] == 0]['cnt'].mean()

# Menghitung rata-rata penggunaan sepeda per hari dalam seminggu
average_daily_usage = bike_data.groupby('weekday')['cnt'].mean().reset_index()

# Judul Dashboard
st.title('Dashboard Penggunaan Sepeda')

# Pertanyaan 1: Jumlah Pengguna Aktif
st.header('Pertanyaan 1: Jumlah Pengguna Aktif')
st.write('Rata-rata Penggunaan Sepeda per Hari: ', average_daily_users)
st.write('Rata-rata Penggunaan Sepeda per Minggu: ', average_weekly_users)

# Visualisasi rata-rata penggunaan sepeda per hari dalam seminggu
st.subheader('Rata-rata Penggunaan Sepeda per Hari dalam Seminggu')
fig = px.line(average_daily_usage, x='weekday', y='cnt', title='Rata-rata Penggunaan Sepeda per Hari dalam Seminggu')
st.plotly_chart(fig)

# Pertanyaan 2: Pola Penggunaan Sepeda
st.header('Pertanyaan 2: Pola Penggunaan Sepeda')
st.write('Rata-rata Penggunaan Sepeda pada Hari Kerja: ', average_usage_workday)
st.write('Rata-rata Penggunaan Sepeda pada Hari Libur: ', average_usage_holiday)


# In[ ]:




