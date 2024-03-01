#!/usr/bin/env python
# coding: utf-8

# Mengimpor library yang diperlukan
import streamlit as st
import pandas as pd
import plotly.express as px

# Memuat data dari file CSV
bike_data = pd.read_csv('main_data.csv')

# Menghitung rata-rata penggunaan sepeda per hari dan per minggu
average_daily_users = bike_data['cnt'].mean()
average_weekly_users = average_daily_users * 7

# Menghitung rata-rata penggunaan sepeda pada hari kerja dan hari libur
average_usage_workday = bike_data[bike_data['workingday'] == 1]['cnt'].mean()
average_usage_holiday = bike_data[bike_data['workingday'] == 0]['cnt'].mean()

# Menghitung rata-rata penggunaan sepeda per hari dalam seminggu
average_daily_usage = bike_data.groupby('weekday')['cnt'].mean().reset_index()

# Menambahkan judul dan header untuk dashboard
st.title('Dashboard Penggunaan Sepeda')
st.header('Pertanyaan 1: Jumlah Pengguna Aktif')

# Menampilkan rata-rata penggunaan sepeda per hari dan per minggu
st.write('Rata-rata Penggunaan Sepeda per Hari: ', average_daily_users)
st.write('Rata-rata Penggunaan Sepeda per Minggu: ', average_weekly_users)

# Visualisasi rata-rata penggunaan sepeda per hari dalam seminggu
st.subheader('Rata-rata Penggunaan Sepeda per Hari dalam Seminggu')
fig = px.line(average_daily_usage, x='weekday', y='cnt', title='Rata-rata Penggunaan Sepeda per Hari dalam Seminggu')
st.plotly_chart(fig)

# Membuat DataFrame untuk visualisasi
usage_comparison = pd.DataFrame({
    'Kondisi': ['Hari Kerja', 'Hari Libur'],
    'Rata-rata Penggunaan Sepeda': [average_usage_workday, average_usage_holiday]
})

# Menampilkan rata-rata penggunaan sepeda pada hari kerja dan hari libur
st.header('Pertanyaan 2: Pola Penggunaan Sepeda')
st.write('Rata-rata Penggunaan Sepeda pada Hari Kerja: ', average_usage_workday)
st.write('Rata-rata Penggunaan Sepeda pada Hari Libur: ', average_usage_holiday)

# Membuat visualisasi menggunakan grafik batang
st.subheader('Perbandingan Penggunaan Sepeda pada Hari Kerja dan Hari Libur (Diagram Batang)')
fig2 = px.bar(usage_comparison, x='Kondisi', y='Rata-rata Penggunaan Sepeda', 
               title='Perbandingan Penggunaan Sepeda pada Hari Kerja dan Hari Libur (Diagram Batang)', 
               color='Kondisi')
st.plotly_chart(fig2)

# Membuat visualisasi menggunakan diagram lingkaran
st.subheader('Perbandingan Penggunaan Sepeda pada Hari Kerja dan Hari Libur (Diagram Lingkaran)')
fig3 = px.pie(usage_comparison, values='Rata-rata Penggunaan Sepeda', names='Kondisi', 
              title='Perbandingan Penggunaan Sepeda pada Hari Kerja dan Hari Libur (Diagram Lingkaran)')
st.plotly_chart(fig3)
