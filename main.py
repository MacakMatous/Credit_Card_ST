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
st.title("Credit Card Dashboard")

# Filters
st.sidebar.header("Filter options")
card_category = st.sidebar.multiselect("Select Card Category Level:", options=df["Card_Category"].unique(), default=df["Card_Category"].unique())
income_category = st.sidebar.multiselect("Select Income Category:", options=df["Income_Category"].unique(), default=df["Income_Category"].unique())
education_levels = st.sidebar.multiselect("Select Education Level:", options=df["Education_Level"].unique(), default=df["Education_Level"].unique())
marital_status = st.sidebar.multiselect("Select Marital Status:", options=df["Marital_Status"].unique(), default=df["Marital_Status"].unique())

# Filtered DataFrame
filtered_df = df[(df["Card_Category"].isin(card_category)) &
                    (df["Income_Category"].isin(income_category)) &
                    (df["Education_Level"].isin(education_levels)) & 
                    (df["Marital_Status"].isin(marital_status))
                ]

# KPI: Customer Attrition Rate
attrition_count = filtered_df["Attrition_Flag"].value_counts()
attrition_rate = (attrition_count.get("Attrited Customer", 0) / attrition_count.sum()) * 100
num_of_pot_churns = len(filtered_df[(filtered_df["Attrition_Flag"] == "Existing Customer") &
                                     (filtered_df["Months_Inactive_12_mon"] > 3)])
avg_util_ratio = filtered_df["Avg_Utilization_Ratio"].mean() * 100

# Display KPIs and plots in three columns
col1, col2, col3 = st.columns([1, 3, 3])

# Column 1: Customer Attrition Rate and Number of Potential Attrition Customers
# FAKE DELTA - Visually pleasing
with col1:
    st.subheader("KPIs")
    st.metric(label="Customer Attrition Rate", delta=-1.5, delta_color="inverse", value=f"{attrition_rate:.2f}%")
    st.metric(label="Number of Potential Attrition", delta=+8, delta_color="inverse", value=f"{num_of_pot_churns}")
    st.metric(label="Avg Utilization Ratio", value=f"{avg_util_ratio:.2f}%")

sns.set_theme("poster")
sns.set_style("darkgrid")

# Column 2: Transaction Volume
with col2:
    st.subheader("Transaction Volume Histogram")
    fig, ax = plt.subplots()
    ax.set(xlabel='Transaction Volume', ylabel='Count')
    sns.histplot(filtered_df["Total_Trans_Ct"], kde=True, ax=ax, color='blue')
    st.plotly_chart(fig)

# Column 3: Average Ticket Size
with col3:
    st.subheader("Avg Open To Buy")
    fig, ax = plt.subplots()
    ax.set(xlabel='Disponible Income', ylabel='Count')
    sns.histplot(filtered_df["Avg_Open_To_Buy"], kde=True, ax=ax, color='green')
    st.plotly_chart(fig)
