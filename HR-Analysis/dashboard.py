import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("HR-Attrition-clean.csv")

st.title("📊 HR Attrition Dashboard")

# KPI
attrition_rate = (df["Attrition"].eq("Yes").mean() * 100).round(1)
st.metric("Overall Attrition Rate", f"{attrition_rate}%")

# Department filter
department = st.selectbox("Select Department:", ["All"] + df["Department"].unique().tolist())
filtered = df if department == "All" else df[df["Department"] == department]

# Plots
fig1 = px.histogram(filtered, x="Age", color="Attrition", barmode="overlay")
st.plotly_chart(fig1)

fig2 = px.bar(filtered, x="JobRole", color="Attrition", barmode="group")
st.plotly_chart(fig2)
