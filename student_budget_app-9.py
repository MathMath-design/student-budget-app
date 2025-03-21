
import streamlit as st
st.set_page_config(page_title="Student Budget App")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Load CSV (semicolon separated)
try:
    df = pd.read_csv('student_data.csv', sep=';')
except:
    df = None
    st.warning("Please upload 'student_data.csv' for group insights.")

st.set_page_config(page_title="Student Budget App")
st.title("📊 Student Budgeting App")

st.markdown("Track your spending, see your savings, and compare with other students.")

st.header("Enter Your Monthly Budget")
income = st.number_input("Monthly Income (€)", min_value=0, value=1000)
rent = st.number_input("Rent (€)", min_value=0, value=450)
tuition = st.number_input("Tuition Fee (€)", min_value=0, value=300)
subs = st.number_input("Subscriptions (€)", min_value=0, value=50)
food = st.number_input("Food (€)", min_value=0, value=200)
supplies = st.number_input("School Supplies (€)", min_value=0, value=40)
transport = st.number_input("Transport (€)", min_value=0, value=60)
other = st.number_input("Other Expenses (€)", min_value=0, value=80)

total_expenses = rent + tuition + subs + food + supplies + transport + other
savings = income - total_expenses

st.subheader("Summary")
st.write(f"**Total Expenses:** €{total_expenses}")
st.write(f"**Estimated Savings:** €{savings}")

if savings < 0:
    st.warning("You're overspending! 🛑")
elif savings < 100:
    st.info("You're just breaking even. Be careful. ⚠️")
else:
    st.success("You're saving well! ✅")

# Pie chart
labels = ['Rent', 'Tuition', 'Subscriptions', 'Food', 'Supplies', 'Transport', 'Other']
sizes = [rent, tuition, subs, food, supplies, transport, other]
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
ax.axis('equal')
st.pyplot(fig)

if df is not None:
    st.header("Insights from 1,000 Students")
    df["total_expenses"] = df[["rent", "tuition_fee", "subscriptions", "food", "school_supplies", "transport", "other_expenses"]].sum(axis=1)
    df["monthly_savings"] = df["monthly_income"] - df["total_expenses"]
    st.metric("Avg Income", f"€{df['monthly_income'].mean():.2f}")
    st.metric("Avg Savings", f"€{df['monthly_savings'].mean():.2f}")
