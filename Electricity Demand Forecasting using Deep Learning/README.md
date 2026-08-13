# Electricity Demand Forecasting Using Deep Learning

## 📌 Project Overview

**Electricity Demand Forecasting Using Deep Learning** is an end-to-end time-series forecasting project designed to predict future electricity demand using historical electricity consumption data.

The project combines **time-series analysis, feature engineering, deep learning, hyperparameter tuning, model evaluation, and Flask deployment** to build an interactive electricity-demand forecasting application.

The system uses historical **PJME electricity demand (`PJME_MW`)** and engineered temporal, lag-based, and rolling-statistical features to forecast future electricity demand.

---

## 🎯 Objectives

The main objectives of this project are:

- Analyze historical electricity consumption patterns.
- Identify daily, weekly, and seasonal demand patterns.
- Perform time-series preprocessing and feature engineering.
- Create lag and rolling statistical features.
- Develop baseline forecasting models.
- Develop deep learning models for multi-step forecasting.
- Compare RNN, LSTM, GRU, and Bi-LSTM models.
- Perform hyperparameter tuning.
- Validate the final forecasting model on unseen periods.
- Build an interactive Flask-based forecasting dashboard.
- Provide visualization and model-performance analytics.

---

## 📊 Dataset

### Dataset Used

**Hourly Energy Consumption – PJM**

The dataset contains hourly electricity consumption values.

### Target Variable

PJME_MW

### Train Variable
Datetime
PJME_MW
Hour
Day
Week
Month
Year
DayOfWeek
IsWeekend
Lag_1
Lag_2
Lag_3
Lag_6
Lag_12
Lag_24
Lag_48
Lag_72
Lag_168
RollingMean_24
RollingMean_168
RollingStd_24

Raw Electricity Dataset
          │
          ▼
   Data Understanding
          │
          ▼
   Data Preprocessing
          │
          ▼
   Feature Engineering
          │
          ├── Time Features
          ├── Lag Features
          └── Rolling Features
          │
          ▼
      EDA Analysis
          │
          ▼
   Baseline Models
          │
          ▼
   Sequence Creation
          │
          ▼
 Deep Learning Models
          │
     ┌────┼────┬────┐
     ▼    ▼    ▼    ▼
    RNN  LSTM  GRU Bi-LSTM
          │
          ▼
 Hyperparameter Tuning
          │
          ▼
   Model Evaluation
          │
          ▼
  30/60-Day Validation
          │
          ▼
     Flask Web App
          │
     ┌────┼──────────────┐
     ▼    ▼              ▼
 Dashboard Forecast   Analytics

# 🔬 Project Phases

## Phase 1 – Data Understanding

The dataset was analyzed to understand:

Dataset structure
Data types
Missing values
Duplicate records
Timestamp information
Electricity-demand distribution
Historical demand trends

The Datetime column was converted into a proper datetime format.

## Phase 2 – Time-Series Preprocessing

The data was sorted chronologically to preserve the temporal relationship.

df = df.sort_values("Datetime")

Time-based features were extracted:

df["Hour"] = df["Datetime"].dt.hour
df["Day"] = df["Datetime"].dt.day
df["DayOfWeek"] = df["Datetime"].dt.dayofweek
df["Week"] = df["Datetime"].dt.isocalendar().week.astype(int)
df["Month"] = df["Datetime"].dt.month
df["Year"] = df["Datetime"].dt.year
df["IsWeekend"] = (df["DayOfWeek"] >= 5).astype(int)


## Phase 3 – Feature Engineering
Lag Features

Historical demand values were used to capture temporal dependencies.

Lag_1
Lag_2
Lag_3
Lag_6
Lag_12
Lag_24
Lag_48
Lag_72
Lag_168

Examples:

Lag_1 → previous hour
Lag_24 → previous day
Lag_168 → previous week
Rolling Features

Rolling statistics were created to capture recent demand behavior.

RollingMean_24
RollingMean_168
RollingStd_24

Rows containing unavailable historical values were removed after feature engineering.

## 📈 Phase 4 – Exploratory Data Analysis

The project analyzes electricity demand using:

Hourly demand trends
Daily demand patterns
Weekly patterns
Monthly patterns
Weekday vs weekend demand
Peak demand periods
Lag relationships
Rolling statistics

These analyses help understand the seasonality and temporal behavior of electricity consumption.

## 🤖 Phase 5 – Baseline Models

Several simple forecasting methods were implemented before developing deep learning models.

Baseline Models
Naive Forecast — Lag 1
Previous-Day Forecast — Lag 24
24-Hour Moving Average
Previous-Week Forecast — Lag 168
Baseline Performance
Model	MAE (MW)	RMSE (MW)	MAPE (%)	R²
Naive (Lag 1)	1207.86	1808.41	3.86	0.92
Previous-Day (Lag 24)	2267.30	3120.65	7.12	0.75
24-Hour Moving Average	3501.35	4456.37	11.44	0.49
Previous-Week (Lag 168)	3542.48	4893.50	10.96	0.39

These baseline models provide a reference point for evaluating the deep learning approaches.

## 🧠 Phase 6 – Deep Learning Models

The project uses a multi-step forecasting approach.

Sequence Configuration

The deep learning experiments considered:

Sequence Length:
24 hours
48 hours
168 hours

Forecast Horizon:
24 hours

The model receives historical information and predicts the next 24 hours of electricity demand.

Models Developed
Simple RNN
LSTM
GRU

This configuration was selected as the final forecasting model for the application.

⚙️ Hyperparameter Tuning

Hyperparameter tuning was performed using Keras Tuner RandomSearch.

The parameters considered included:

Bi-LSTM Units:
32, 64, 128

Dense Units:
32, 64, 128

Learning Rate:
0.0001
0.0005
0.001

The tuning objective was:

val_loss

The best-performing hyperparameter configuration was selected for the final model.

##  🔄 Data Scaling

Two separate StandardScaler objects were used.

Feature Scaler
Models/X_scaler.pkl

Used to scale the 19 input features.

Target Scaler
Models/y_scaler.pkl

Used to scale the PJME_MW target.

The scalers are saved using joblib so the same preprocessing can be applied during Flask inference.

## 📅 Phase 7 – Validation

The validation stage evaluates the final forecasting model on an unseen chronological period.

The project maintains chronological ordering:

Historical Training Data
          ↓
Validation Period
          ↓
Final Test Period

The Flask validation interface supports:

30-Day Validation
60-Day Validation

The selected validation period is used to compare actual electricity demand with model predictions.

Validation Metrics
MAE
RMSE
MAPE
Validation Visualizations
Actual vs Predicted Demand
30-Day Forecast Performance
60-Day Forecast Performance
Daily Forecast Error
Peak Demand Error
Forecast Error Distribution

The validation process helps evaluate how well the final model performs on an unseen period rather than only on the training data.

## 🌐 Flask Web Application

The project includes an interactive forecasting dashboard developed using:

Flask
HTML
CSS
Bootstrap
JavaScript
Chart.js
Pandas
NumPy
TensorFlow/Keras
Scikit-learn
Joblib
### 📊 Dashboard

The dashboard provides an overview of electricity demand.

Dashboard Features
Current/latest demand
Historical consumption
Maximum demand
Minimum demand
Forecast summary
Model performance  

### 🔮 Forecast Page

The Forecast page allows the user to select a forecasting horizon.

Available options:

24 Hours
48 Hours
72 Hours

The application generates future electricity-demand predictions and displays:

Forecast Summary
Forecast Horizon
Average Forecast
Peak Forecast
Forecast Visualization

A Chart.js line chart displays the predicted future electricity demand.

Forecast Table
Time	Forecast Demand (MW)
Future timestamp	Predicted MW
Future timestamp	Predicted MW
...	...

The forecast timestamps are generated automatically from the latest timestamp in the dataset.

### 📈 Analytics Page

The Analytics page provides detailed demand and model analysis.

Historical Demand

Displays recent electricity consumption trends.

Model Comparison

Compares forecasting models using:

MAE
RMSE
MAPE
R²
Forecast Error

Forecast error is calculated as:

Forecast Error = Actual Demand - Predicted Demand

The error values are visualized using an interactive Chart.js graph.

Peak Demand Analysis

The application provides analysis of high-demand periods to understand forecasting performance during peak electricity consumption.

### 📋 Validation Page

The Validation page allows the user to select:

30 Days

or

60 Days

The selected validation period displays:

Metrics
MAE
RMSE
MAPE
Visualizations
Actual vs Predicted
Forecast Error
Daily Error
Peak Demand Performance
Error Distribution

This provides a clear evaluation of forecasting performance on an unseen period.

### 📁 Project Structure

Electricity Demand Forecasting using Deep Learning/
│
├── Dataset/
│   ├── PJME_hourly.csv
│   ├── df_for_EDA.csv
│   └── final_df.csv
│
├── Models/
│   ├── X_scaler.pkl
│   ├── y_scaler.pkl
│   └── best_model.keras
│
├── Notebooks/
│   ├── Data_Understanding.ipynb
│   ├── Preprocessing.ipynb
│   ├── EDA.ipynb
│   ├── Baseline_Models.ipynb
│   ├── Deep_Learning_Models.ipynb
│   ├── Hyperparameter_Tuning.ipynb
│   └── Validation.ipynb
│
├── flask_app/
│   ├── app.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── forecast.html
│   │   ├── analytics.html
│   │   └── validation.html
│   │
│   └── static/
│       ├── css/
│       │   └── style.css
│       │
│       └── js/
│           └── charts.js
│
├── requirements.txt
│
└── README.md


## 🛠️ Technologies Used
Technology	Purpose
Python	Main programming language
Pandas	Data preprocessing and analysis
NumPy	Numerical computation
Matplotlib	Data visualization
Scikit-learn	Scaling and evaluation
TensorFlow/Keras	Deep learning
Keras Tuner	Hyperparameter tuning
Joblib	Saving and loading scalers
Flask	Web application
Bootstrap	User interface
JavaScript	Frontend interaction
Chart.js	Interactive charts
HTML/CSS	Web interface

## 📦 Installation

Clone the repository:

git clone <your-github-repository-url>

Move into the project directory:

cd "Electricity Demand Forecasting using Deep Learning"


Install the required packages with pipenv:

>>> pipenv install
>>> pipenv shell

▶️ Running the Flask Application

Navigate to the Flask application directory:

cd flask_app

Run the application:

python app.py

## Open the local Flask URL displayed in the terminal.

## 🔮 Using the Forecast Application

#### Step 1

Open the Forecast page.

#### Step 2

Select a forecasting horizon:

24 Hours
48 Hours
72 Hours

#### Step 3

Click:

Generate Forecast

#### Step 4

The application generates:

Future timestamps
Forecast demand
Average forecast
Peak forecast
Forecast chart
Forecast table

#### 📊 Using Validation

Open the Validation page.

Select either:

30 Days

or:

60 Days

The application displays:

Actual Demand
Predicted Demand
MAE
RMSE
MAPE
Forecast Error

The results can be visualized through the validation charts.

📌 Key Results

The experiments showed that deep learning models can capture temporal patterns in electricity consumption.

The best-performing deep learning configuration was the 168-hour Bi-LSTM:

MAE  = 1716.29 MW
RMSE = 2290.09 MW
MAPE = 5.66 %
R²   = 0.8746
bias = 216.421

The model was integrated into the Flask application to provide interactive electricity-demand forecasting.

Author

Logesh M