import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

st.set_page_config(layout="wide")
st.title("🛡️ Real-Time Fraud Detection Dashboard")

DATA_PATH = '../data/fraud_output.csv'

if not os.path.exists(DATA_PATH):
    st.warning("⚠️ Run the fraud engine first to generate data.")
else:
    df = pd.read_csv(DATA_PATH)
    
    st.subheader("📊 Transaction Summary")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Transactions", len(df))
    with col2:
        st.metric("Detected Frauds", int(df['is_fraud'].sum()))

    st.markdown("---")
    st.subheader("🔎 Browse Transactions")
    fraud_filter = st.selectbox("Filter by Fraud Label", ["All", "Fraud", "Non-Fraud"])
    if fraud_filter == "Fraud":
        st.dataframe(df[df['is_fraud'] == 1])
    elif fraud_filter == "Non-Fraud":
        st.dataframe(df[df['is_fraud'] == 0])
    else:
        st.dataframe(df)

    st.markdown("---")
    st.subheader("📈 Fraud Distribution by Hour")
    fig1, ax1 = plt.subplots()
    sns.countplot(data=df, x='hour', hue='is_fraud', palette='Set1', ax=ax1)
    ax1.set_xlabel("Hour of Day")
    ax1.set_ylabel("Transaction Count")
    ax1.legend(["Non-Fraud", "Fraud"])
    st.pyplot(fig1)

    st.subheader("💰 Amount vs Fraud Status")
    fig2, ax2 = plt.subplots()
    sns.boxplot(data=df, x='is_fraud', y='amount', palette='Set2', ax=ax2)
    ax2.set_xticklabels(["Non-Fraud", "Fraud"])
    ax2.set_ylabel("Amount")
    st.pyplot(fig2)
