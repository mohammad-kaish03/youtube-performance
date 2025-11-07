📺 YouTube Channel Performance Secrets — Data Analytics & Machine Learning
📘 Project Overview

This project analyzes YouTube channel performance metrics to uncover factors that influence engagement, audience retention, and revenue generation.
It combines data analytics, feature engineering, and machine learning to predict YouTube revenue based on video and channel-level metrics such as views, engagement rate, likes, and shares.

A deployed Streamlit app allows users to input their YouTube metrics and get instant revenue predictions using a trained Random Forest Regressor model.

🎯 Objectives

Perform Exploratory Data Analysis (EDA) to identify the strongest predictors of revenue.

Visualize trends and correlations between engagement metrics and earnings.

Engineer features to improve model interpretability (e.g., engagement rate, revenue per view).

Train a Random Forest Regressor to estimate YouTube revenue.

Build an interactive Streamlit dashboard for predictions.

📁 Dataset Description

File: youtube_channel_real_performance_analytics.csv
Source: YouTube Channel Analytics Dataset (Google Drive)

Rows: 364  Columns: 70

Key Columns:
Category	Columns
Video Details	Video Duration, Publish Time, Day, Month, Year, Day of Week
Revenue Metrics	Estimated Revenue (USD), Revenue per 1000 Views (USD), Ad Impressions, CPM (USD)
Engagement Metrics	Views, Likes, Shares, Comments, Watch Time (hours), CTR (%)
Audience Data	Subscribers, New Viewers, Returning Viewers, Unique Viewers
Monetization	YouTube Premium Revenue, Transactions, Total Sales Volume (USD)
🧠 Tech Stack

Language: Python

Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn, joblib

Model: Random Forest Regressor

Dashboard: Streamlit

Environment: Jupyter Notebook / VS Code

⚙️ Project Workflow
1. Data Preprocessing

Removed missing values and converted columns (e.g., video duration → seconds).

Extracted new features:

Revenue per View = Estimated Revenue / Views

Engagement Rate = (Likes + Shares + Comments) / Views × 100

2. Exploratory Data Analysis (EDA)

Revenue distribution histograms

Correlation heatmaps for all numeric metrics

Scatter plots for Views vs Revenue

Identified top-performing videos and engagement patterns

3. Feature Engineering

Created aggregated metrics for:

Engagement effectiveness

Revenue conversion efficiency

Video performance duration normalization

4. Model Building

Used RandomForestRegressor for revenue prediction:

from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


Performance:

RMSE: 0.456

R² Score: ~0.88 (strong predictive capability)

The trained model was exported as:

youtube_revenue_predictor.pkl

5. Deployment (Streamlit App)

Interactive web interface for real-time revenue prediction.

Streamlit App Features:

Inputs: Views, Subscribers, Likes, Shares, Comments, Engagement Rate

Outputs: Predicted Estimated Revenue (USD)

Run the app:

streamlit run streamlit.py


or double-click:

app.bat

💻 Example Prediction

Input:

Metric	Value
Views	50,000
Subscribers	3,000
Likes	1,200
Shares	250
Comments	80
Engagement Rate	5.3

Output:
💰 Predicted Estimated Revenue: $147.28 USD

📊 Visual Insights

Revenue vs Views: Positive linear relationship — high view count strongly correlates with higher earnings.

Engagement Rate: Direct impact on monetization efficiency.

Top Drivers of Revenue:

Views

Engagement Rate

Subscribers

Watch Time

Outliers: Viral videos skew averages — normalization helps stabilize trends.

🔍 Key Takeaways

✅ Engagement and retention are the strongest predictors of revenue.
✅ High CTR and video duration above average tend to increase earnings.
✅ Machine learning allows reliable revenue forecasting from public YouTube analytics.

Install dependencies

pip install -r requirements.txt


Run Jupyter Notebook (for analysis)

jupyter notebook YouTube_Channel_Performance_Secrets.ipynb


Launch the Streamlit Dashboard

streamlit run streamlit.py

🧾 Files Included
File	Description
YouTube_Channel_Performance_Secrets.ipynb	Full EDA and model training notebook
youtube_channel_real_performance_analytics.csv	Dataset used for training
youtube_revenue_predictor.pkl	Trained ML model
streamlit.py	Streamlit web app for predictions
requirements.txt	Dependencies list
app.bat	One-click launcher for Windows
README.md	Project documentation
💡 Future Improvements

Integrate YouTube Data API for live analytics.

Add Sentiment Analysis on video comments.

Include forecasting models for subscriber and revenue growth.

Deploy on Streamlit Cloud or Hugging Face Spaces for public use.


🏷️ License

Licensed under the MIT License — you may use, modify, and distribute with attribution.
