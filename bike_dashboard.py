import streamlit as st
import pandas as pd

# Load the dataset
data = pd.read_csv("bike_data_bersih.csv")

# Create a Streamlit app
st.title("Bike Dashboard")

# Question 1: Average number of active users in one day or one week
if st.button("Average number of active users in one day"):
    average_daily_users = data['active_users'].mean()
    st.write(f"The average number of active users in one day is: {average_daily_users}")

if st.button("Average number of active users in one week"):
    average_weekly_users = data['active_users'].mean() * 7
    st.write(f"The average number of active users in one week is: {average_weekly_users}")

# Question 2: Bicycle usage patterns between weekdays and holidays
if st.button("Check bicycle usage patterns"):
    weekday_usage = data[data['day_type'] == 'weekday']['usage_pattern'].value_counts()
    holiday_usage = data[data['day_type'] == 'holiday']['usage_pattern'].value_counts()
    
    st.write("Bicycle usage patterns on weekdays:")
    st.write(weekday_usage)
    
    st.write("Bicycle usage patterns on holidays:")
    st.write(holiday_usage)
