import fitbit_data
import streamlit as st # Requires installation of streamlit module
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# To run: streamlit run fitbit_dashboard.py

st.title("Imad's Fitbit dashboard")

'''
Figure 1:

Step count for a 30-day period
'''

today = datetime.now()

year = today.year
month = str(today.month).rjust(2, '0') # Ensure 2 digits for month and day
day = str(today.day).rjust(2, '0')

# Construct date string and retrieve step count
date = f'{year}-{month}-{day}'
df_steps = fitbit_data.get_user_steps(date)

# Plot step count data in a horizontal barplot, and show average value
fig1 = plt.figure()
ax = sns.barplot(df_steps, x='Steps', y='Date', orient='h', color='blue', alpha=0.6)
avg_steps = df_steps['Steps'].mean()
ax.axvline(x=avg_steps, linewidth=2, color='orange', ls=':')
st.subheader('Step count from last 30 days')
st.pyplot(fig1)

st.markdown('---')

'''
Figure 2:

Heart rate data for selected day
'''
day = st.date_input(label = 'Select a day:')
st.write(day)

# Get HR data and then compute 10-minute rolling average
df_hr = fitbit_data.get_hr_per_min(day)
df_hr['HR_10_min_avg'] = df_hr.rolling(window=10)['HR'].mean()

# Create lineplot of averaged 10-minute data, showing mean HR for the day
fig2 = plt.figure()
st.subheader(f'Heart rate for {day} (10-minute average).')

# Reduce label clutter and proportion for improved readability
sns.set(font_scale = 0.7)
df_hr['time'] = df_hr['time'].str.slice(0, 5)
plot_ = sns.lineplot(df_hr, x='time', y='HR_10_min_avg')
avg_hr = df_hr['HR_10_min_avg'].mean()

# Show average heart rate as a horizontal line
plot_.axhline(y=avg_hr, linewidth=2, color='orange', ls=':')

# Reduce density of x-label ticks for readability
for ind, label in enumerate(plot_.get_xticklabels()):
    if ind % 120 == 0:  # every 120th label is kept
        label.set_visible(True)
    else:
        label.set_visible(False)

# Display tick marks vertically
plt.xticks(rotation=90)
st.pyplot(fig2)
