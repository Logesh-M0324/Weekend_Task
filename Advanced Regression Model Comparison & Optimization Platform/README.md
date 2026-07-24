# 🏠 Advanced Regression Model Comparison & Optimization Platform

An end-to-end Machine Learning project for predicting house prices using multiple regression algorithms. The project compares the performance of various regression models, applies optimization techniques to improve prediction accuracy, and deploys the best-performing model through a Flask web application.

---

## 📌 Project Overview

House price prediction is an important application of Machine Learning in the real estate industry. The objective of this project is to build an accurate and reliable regression model capable of estimating house prices based on property characteristics.

The project follows a complete machine learning workflow, including:

- Data Understanding
- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Model Development
- Model Optimization
- Model Evaluation & Comparison
- Model Deployment using Flask
- Version Control using Git & GitHub

---

## 🎯 Objectives

- Analyze the House Prices dataset.
- Perform data preprocessing and feature engineering.
- Train multiple regression models.
- Compare model performance using evaluation metrics.
- Optimize models using Cross Validation and Hyperparameter Tuning.
- Select the best-performing model.
- Deploy the final model using Flask.
- Build a responsive web application for real-time house price prediction.

---

## 📂 Dataset

**Dataset Name:** House Prices – Advanced Regression Techniques

**Source:** Kaggle

**Target Variable:** SalePrice

**Dataset Summary**

| Attribute | Value |
|-----------|--------|
| Training Samples | 1460 |
| Test Samples | 1459 |
| Original Features | 80 |
| Target Variable | SalePrice |

---

# 🛠 Technologies Used

### Programming Language

- Python 3.x

### Machine Learning Libraries

- Scikit-learn
- XGBoost
- LightGBM
- CatBoost
- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn

### Web Framework

- Flask
- Bootstrap 5
- HTML
- CSS

### Development Tools

- Jupyter Notebook
- VS Code
- Git
- GitHub

---

# 📊 Project Workflow

```
Dataset
     │
     ▼
Data Understanding
     │
     ▼
Data Preprocessing
     │
     ▼
Exploratory Data Analysis
     │
     ▼
Model Development
     │
     ▼
Model Optimization
     │
     ▼
Model Evaluation
     │
     ▼
Best Model Selection
     │
     ▼
Flask Deployment
```

---

# 🚀 Project Phases

## ✅ Phase 1 – Data Understanding

- Business Problem Analysis
- Dataset Exploration
- Feature Description
- Missing Value Analysis
- Duplicate Check
- Descriptive Statistics
- Target Variable Distribution

### Visualizations

- Histograms
- Box Plots
- Correlation Heatmap
- Pair Plot
- Missing Value Heatmap

---

## ✅ Phase 2 – Data Preprocessing

- Missing Value Handling
- Duplicate Removal
- Outlier Treatment
- Categorical Encoding
- Feature Scaling
- Skewness Handling

---

## ✅ Phase 3 – Exploratory Data Analysis

- Feature vs Target Analysis
- Correlation Analysis
- Outlier Analysis
- Feature Importance
- Relationship Analysis

### Visualizations

- Scatter Plots
- Heatmaps
- Histograms
- Pair Plots
- Distribution Charts

---

## ✅ Phase 4 – Model Development

The following regression models were trained and compared:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor
- LightGBM Regressor
- CatBoost Regressor

Evaluation Metrics

- MAE
- MSE
- RMSE
- R² Score

---

## ✅ Phase 5 – Model Improvement & Optimization

Optimization techniques applied:

- Feature Engineering
- Feature Selection
- Data Transformation
- Outlier Treatment
- Missing Value Handling
- Multicollinearity Analysis (VIF)
- Cross Validation
- Hyperparameter Tuning

---

## ✅ Phase 6 – Model Evaluation & Comparison

Models were evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score
- Cross Validation Score

Visualizations include:

- Actual vs Predicted Plot
- Residual Plot
- Feature Importance
- Model Comparison Charts

---

## 🌐 Flask Web Application

The trained model was deployed using Flask to provide real-time house price predictions.

### Features

🏠 Home Page

- Project Overview
- Dataset Summary
- Navigation

📊 Dashboard

- Dataset Information
- Model Summary
- Performance Metrics

🔮 Prediction Module

- User Input Form
- Real-Time Price Prediction
- Prediction Result

📈 Comparison Dashboard

- Model Comparison
- Performance Metrics
- Best Model Highlight

📉 Analytics Dashboard

- Correlation Heatmap
- Feature Importance
- Residual Analysis
- Distribution Charts

📄 Reports

- Prediction Report
- Model Evaluation Report
- Comparison Report

---

# 📁 Project Structure

```
Advanced-Regression-Model/

│── app.py
│── model.pkl
│── requirements.txt
│── README.md
│
├── static/
│   ├── css/
│   ├── images/
│   ├── reports/
│          ├── Model_Evaluation_Report.pdf
│          ├── Comparison_Report.pdf
│          └── Prediction_Report.pdf
├── templates/
│   ├── home.html
│   ├── dashboard.html
│   ├── predict.html
│   ├── result.html
│   ├── comparison.html
│   ├── analytics.html
│   └── reports.html
│
├── notebooks/
│   ├── Phase1_Data_Understanding.ipynb
│   ├── Phase2_Preprocessing.ipynb
│   ├── Phase3_EDA.ipynb
│   ├── Phase4_Model_Development.ipynb
│   ├── Phase5_Optimization.ipynb
│   └── Phase6_Evaluation.ipynb
│
├──  Advanced Regression Model Comparison & Optimization Platform.docx
├── Advanced Regression Model Comparison & Optimization Platform.pdf
├── Pipfile
├── Pipfile.lock
├──README.md
---

# 📈 Final Model

Two best-performing models were observed during the project.

### Baseline Model

- **CatBoost Regressor**
- Highest R² score using the complete preprocessed dataset.

### Final Deployed Model

- **XGBoost Regressor**

The XGBoost model was selected after applying feature engineering, feature selection, cross validation, and hyperparameter tuning. It demonstrated better generalization, lower complexity, and was well suited for deployment in the Flask application.

---

# 🎯 Top Features Used for Prediction

The final model uses the following ten important features:

- Overall Quality
- Garage Capacity
- Garage Area
- Lot Area
- Masonry Veneer Area
- Garage Built Year
- Number of Fireplaces
- Total Rooms Above Ground
- Kitchen Quality
- Basement Quality

These features provide a good balance between prediction accuracy and user-friendly input.

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/Logesh-M0324/Weekend_Task/tree/main/Advanced%20Regression%20Model%20Comparison%20%26%20Optimization%20Platform
```

Move into the project directory

```bash
cd Advanced Regression Model Comparison & Optimization Platform
```

Install dependencies

```bash
pipenv install

pipenv shell
```

Run the Flask application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

# 📊 Future Enhancements

- Cloud Deployment (AWS/Azure)
- User Authentication
- Real-time Dataset Updates
- REST API Integration
- Deep Learning Models
- Explainable AI (SHAP/LIME)
- Interactive Dashboard

---

# ✅ Conclusion

This project successfully developed an end-to-end machine learning solution for house price prediction by comparing multiple regression algorithms and applying optimization techniques to improve model performance. The final XGBoost model was deployed through a Flask web application, enabling users to obtain real-time house price predictions using a simple and interactive interface. The project demonstrates the complete machine learning lifecycle, from data preprocessing and model development to deployment and practical application.

---

# 👨‍💻 Author

**LOGESH M**

---
