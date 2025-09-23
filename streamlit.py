import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('youtube_revenue_predictor.pkl')

# App title
st.title("📺 YouTube Revenue Predictor")
st.markdown("Enter video metrics below to estimate expected revenue.")

# Input form
with st.form("prediction_form"):
    views = st.number_input("Views", min_value=0, value=10000)
    subscribers = st.number_input("Subscribers", min_value=0, value=500)
    likes = st.number_input("Likes", min_value=0, value=300)
    shares = st.number_input("Shares", min_value=0, value=50)
    comments = st.number_input("New Comments", min_value=0, value=20)
    engagement_rate = st.number_input("Engagement Rate (%)", min_value=0.0, value=3.7)

    submitted = st.form_submit_button("Predict Revenue")

# Prediction
if submitted:
    input_data = pd.DataFrame({
        'Views': [views],
        'Subscribers': [subscribers],
        'Likes': [likes],
        'Shares': [shares],
        'New Comments': [comments],
        'Engagement Rate': [engagement_rate]
    })

    prediction = model.predict(input_data)[0]
    st.success(f"💰 Estimated Revenue: **${prediction:.2f} USD**")