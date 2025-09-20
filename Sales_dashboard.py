import streamlit as st
import pandas as pd
import plotly.express as px

#Load data
df = pd.read_csv('Sales_data.csv')

#Sidebar filters
st.sidebar.header("Filters")
region = st.sidebar.multiselect("Select Region",df["Region"].unique())
product = st.sidebar.multiselect("Select Product",df["Product"].unique())

#Filter data
filtered_df = df[(df["Region"].isin(region)) & (df["Product"].isin(product))]

#Dashboard
st.title(":blue[SALES DASHBOARD]")
st.write("### Sales by Region")
fig1 = px.bar(filtered_df, x = "Region", y = "Total_Sales",color = "Product",barmode = "group")
st.plotly_chart(fig1)

st.write("### Monthly Sales Trend")
fig2 = px.bar(filtered_df, x = "Month",y = "Total_Sales",color = "Product",barmode = "group")
st.plotly_chart(fig2)