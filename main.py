import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("Bank_Churners.csv")
# Set Streamlit app title and favicon
st.set_page_config(page_title="Credit Card Customers Dashboard", 
                   page_icon=":bar_chart:",
                   layout="wide")

# Streamlit app
st.title("Customer Analysis Dashboard")

# Filters
st.sidebar.header("Filter options")
education_levels = st.sidebar.multiselect("Select Education Level:", options=df["Education_Level"].unique(), default=df["Education_Level"].unique())
marital_status = st.sidebar.multiselect("Select Marital Status:", options=df["Marital_Status"].unique(), default=df["Marital_Status"].unique())
income_category = st.sidebar.multiselect("Select Income Category:", options=df["Income_Category"].unique(), default=df["Income_Category"].unique())

# Filtered DataFrame
filtered_df = df[(df["Education_Level"].isin(education_levels)) & (df["Marital_Status"].isin(marital_status)) & (df["Income_Category"].isin(income_category))]

# Customer Attrition Rate
st.subheader("Customer Attrition Rate")
attrition_rate = filtered_df["Attrition_Flag"].value_counts(normalize=True) * 100
st.bar_chart(attrition_rate)

# Transaction Volume
st.subheader("Transaction Volume (Total Transactions Count)")
st.bar_chart(filtered_df["Total_Trans_Ct"])

# Average Ticket Size
st.subheader("Average Ticket Size (Avg Open To Buy)")
st.bar_chart(filtered_df["Avg_Open_To_Buy"])

# Education Level Distribution
st.subheader("Distribution of Education Levels")
fig, ax = plt.subplots()
sns.countplot(data=filtered_df, x='Education_Level', palette='viridis', order=filtered_df['Education_Level'].value_counts().index, ax=ax)
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='baseline', fontsize=12, color='black', xytext=(0, 5), textcoords='offset points')
st.pyplot(fig)

# Marital Status Distribution
st.subheader("Distribution of Marital Status")
fig, ax = plt.subplots()
sns.countplot(data=filtered_df, x='Marital_Status', palette='viridis', order=filtered_df['Marital_Status'].value_counts().index, ax=ax)
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='baseline', fontsize=12, color='black', xytext=(0, 5), textcoords='offset points')
st.pyplot(fig)

# Income Category Distribution
st.subheader("Distribution of Income Categories")
fig, ax = plt.subplots()
sns.countplot(data=filtered_df, x='Income_Category', palette='viridis', order=filtered_df['Income_Category'].value_counts().index, ax=ax)
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='baseline', fontsize=12, color='black', xytext=(0, 5), textcoords='offset points')
st.pyplot(fig)

# Running the app: Save this script as `app.py` and then run `streamlit run app.py` from your command line.