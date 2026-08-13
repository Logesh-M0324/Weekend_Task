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

```text
PJME_MW

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

 🔬 Project Phases
Phase 1 – Data Understanding

The dataset was analyzed to understand:

Dataset structure
Data types
Missing values
Duplicate records
Timestamp information
Electricity-demand distribution
Historical demand trends

The Datetime column was converted into a proper datetime format.

Phase 2 – Time-Series Preprocessing

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
Phase 3 – Feature Engineering
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

📈 Phase 4 – Exploratory Data Analysis

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

🤖 Phase 5 – Baseline Models

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

🧠 Phase 6 – Deep Learning Models

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
Bidirectional LSTM
🏆 Deep Learning Model Comparison
Sequence Length: 24 Hours
Model	MAE	RMSE	MAPE (%)	R²	Bias
RNN	2846.43	3783.65	9.48	0.6564	947.41
LSTM	3283.34	4331.46	11.14	0.5498	2062.53
GRU	4117.81	5192.92	14.13	0.3528	2411.61
Bi-LSTM	2695.59	3642.70	8.97	0.6816	1326.54
Sequence Length: 48 Hours
Model	MAE	RMSE	MAPE (%)	R²	Bias
RNN	3113.50	4235.22	10.39	0.5699	951.41
LSTM	3116.87	4212.93	10.46	0.5744	1788.96
GRU	3431.37	4571.75	11.60	0.4989	1739.28
Bi-LSTM	2483.91	3341.67	8.35	0.7323	1040.45
Sequence Length: 168 Hours
Model	MAE	RMSE	MAPE (%)	R²	Bias
RNN	2505.47	3429.29	8.37	0.7188	1325.39
LSTM	3084.04	4103.48	10.45	0.5973	1673.61
GRU	3645.56	4866.69	12.35	0.4336	2286.38
Bi-LSTM	2600.28	3471.10	8.82	0.7119	1223.36
Best Deep Learning Configuration

Based on the experiments, the 48-hour Bi-LSTM achieved the strongest overall deep-learning performance:

Model       : Bi-LSTM
Sequence    : 48 hours
MAE         : 2483.91 MW
RMSE        : 3341.67 MW
MAPE        : 8.35 %
R²          : 0.7323
Bias        : 1040.45 MW

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

🔄 Data Scaling

Two separate StandardScaler objects were used.

Feature Scaler
Models/X_scaler.pkl

Used to scale the 19 input features.

Target Scaler
Models/y_scaler.pkl

Used to scale the PJME_MW target.

The scalers are saved using joblib so the same preprocessing can be applied during Flask inference.

📅 Phase 7 – Validation

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

🌐 Flask Web Application

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
📊 Dashboard

The dashboard provides an overview of electricity demand.

Dashboard Features
Current/latest demand
Historical consumption
Maximum demand
Minimum demand
Forecast summary
Model performance
🔮 Forecast Page

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

📈 Analytics Page

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

📋 Validation Page

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

📁 Project Structure
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
🛠️ Technologies Used
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
📦 Installation

Clone the repository:

git clone <your-github-repository-url>

Move into the project directory:

cd "Electricity Demand Forecasting using Deep Learning"

Create a virtual environment:

python -m venv venv
Windows
venv\Scripts\activate
Linux/macOS
source venv/bin/activate

Install the required packages:

pip install -r requirements.txt
📄 Requirements

The requirements.txt file contains the major dependencies:

flask
pandas
numpy
scikit-learn
tensorflow
keras
keras-tuner
joblib
matplotlib
▶️ Running the Flask Application

Navigate to the Flask application directory:

cd flask_app

Run the application:

python app.py

Open the local Flask URL displayed in the terminal.

🔮 Using the Forecast Application
Step 1

Open the Forecast page.

Step 2

Select a forecasting horizon:

24 Hours
48 Hours
72 Hours
Step 3

Click:

Generate Forecast
Step 4

The application generates:

Future timestamps
Forecast demand
Average forecast
Peak forecast
Forecast chart
Forecast table
📊 Using Validation

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

⚠️ Important Design Considerations
Chronological Data Splitting

Random train-test splitting is avoided because this is a time-series forecasting problem.

The data is kept in chronological order to prevent future information from leaking into the training process.

Scaling

The scalers are fitted only on the training data and then used to transform validation and test data.

Multi-Step Forecasting

The final deep learning configuration uses:

Previous 48 Hours → Next 24 Hours
Model and Scaler Compatibility

The Flask application must use the same:

Feature columns
Feature order
Sequence length
X_scaler
y_scaler

that were used during model training.

📌 Key Results

The experiments showed that deep learning models can capture temporal patterns in electricity consumption.

The best-performing deep learning configuration was the 48-hour Bi-LSTM:

MAE  = 2483.91 MW
RMSE = 3341.67 MW
MAPE = 8.35 %
R²   = 0.7323

The model was integrated into the Flask application to provide interactive electricity-demand forecasting.

🚀 Future Improvements

Possible future improvements include:

Incorporating weather information.
Adding temperature and humidity features.
Testing Transformer-based forecasting models.
Implementing probabilistic forecasting.
Adding prediction/confidence intervals.
Deploying the application using Docker.
Deploying the application to a cloud platform.
Adding automated model retraining.
Integrating real-time electricity-demand data.
Improving long-horizon forecasting performance.

Author

Logesh M