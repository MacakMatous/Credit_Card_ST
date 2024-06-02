import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Set Streamlit app title and favicon
st.set_page_config(page_title="Credit Card Customers Dashboard", 
                   page_icon=":bar_chart:",
                   layout="wide")

# Set Streamlit app title
st.title('Credit Card Dashboard')

df = pd.read_csv("Bank_Churners.csv")
st.dataframe(df.head())

# Display some KPIs
st.write("## Key Performance Indicators")
total_transactions = df['Total_Trans_Amt'].sum()
average_utilization = df['Avg_Utilization_Ratio'].mean()
st.write(f"Total Transaction Amount: ${total_transactions:.2f}")
st.write(f"Average Utilization Ratio: {average_utilization:.2%}")

# Create a bar chart for education levels
st.write("## Education Level Distribution")
edu_counts = df['Education_Level'].value_counts()
fig, ax = plt.subplots(ncols=2, figsize=(12, 6))
ax[0].bar(edu_counts.index, edu_counts.values)
plt.xlabel("Education Level")
plt.ylabel("Count")

ax[1].scatter(df['Customer_Age'], df['Credit_Limit'], alpha=0.5)
plt.xlabel("Customer Age")
plt.ylabel("Credit Limit")
st.pyplot(fig)