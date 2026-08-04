# 🩺 Skin Disease Classification & Diagnosis Platform

An end-to-end Deep Learning web application that classifies different types of skin diseases from dermoscopic images using Convolutional Neural Networks (CNNs) and Transfer Learning models. The application provides AI-powered disease prediction, confidence scores, Grad-CAM visualizations for explainable AI, model performance analytics, and downloadable reports through a Flask-based web interface.

---

# 📌 Project Overview

This project implements the complete deep learning workflow for medical image classification, from data preprocessing and model training to deployment using Flask. Multiple CNN architectures and transfer learning models are trained and compared to identify the best-performing model based on various evaluation metrics.

The application enables users to upload a skin lesion image, predict the disease class, visualize the model's attention using Grad-CAM, and explore model performance through an interactive dashboard.

---

# 🎯 Objectives

* Classify seven different skin disease categories.
* Compare multiple CNN and Transfer Learning models.
* Improve model performance using optimization techniques.
* Explain model predictions using Grad-CAM.
* Deploy the trained model using Flask.
* Provide downloadable diagnosis and model comparison reports.

---

# 🧬 Dataset

**Dataset:** HAM10000 (Human Against Machine with 10,000 Training Images)

**Number of Classes:** 7

* Melanoma
* Melanocytic Nevus
* Basal Cell Carcinoma
* Benign Keratosis
* Actinic Keratosis
* Dermatofibroma
* Vascular Lesion

---

# 🚀 Features

## Deep Learning

* Image preprocessing
* Image augmentation
* Custom CNN models
* Transfer Learning
* Model optimization
* Hyperparameter tuning
* Explainable AI using Grad-CAM

## Flask Application

* Modern responsive UI
* Dashboard
* Image upload
* Disease prediction
* Confidence score
* Class probability visualization
* Grad-CAM visualization
* Analytics dashboard
* Reports page
* Download diagnosis report
* Download model comparison report

---

# 🏗️ Project Structure

```text
Skin Disease Classification & Diagnosis Platform/

├── flask_app/
│   ├── app.py
│   ├── models/
│   ├── utils/
│   ├── reports/
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── dashboard.html
│   │   ├── upload.html
│   │   ├── result.html
│   │   ├── analytics.html
│   │   └── reports.html
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   ├── uploads/
│   │   ├── gradcam/
│   │   ├── plots/
│   │   └── images/
│   └── saved_models/
│
├── notebooks/
│
├── dataset/
│
├── figures/
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Technologies Used

## Programming Language

* Python

## Deep Learning

* TensorFlow
* Keras

## Image Processing

* OpenCV
* NumPy

## Data Analysis

* Pandas

## Visualization

* Matplotlib
* Seaborn

## Web Development

* Flask
* Bootstrap 5

## Explainable AI

* Grad-CAM

## Version Control

* Git
* GitHub

---

# 📊 Deep Learning Workflow

### Phase 1 – Data Understanding

* Dataset exploration
* Class distribution analysis
* Image quality analysis
* Dataset splitting

### Phase 2 – Data Preprocessing

* Image resizing
* Normalization
* Data augmentation
* Class imbalance handling
* TensorFlow data pipelines

### Phase 3 – Exploratory Data Analysis

* Pixel intensity analysis
* Image augmentation comparison
* Class-wise image visualization

### Phase 4 – Model Development

Custom Models

* Basic CNN
* Deep CNN
* CNN + Batch Normalization
* CNN + Dropout

Transfer Learning Models

* MobileNetV2
* EfficientNetB0
* ResNet50
* DenseNet121

### Phase 5 – Model Improvement

* Data augmentation
* Batch normalization
* Dropout
* Early stopping
* Learning rate scheduling
* Optimizer comparison
* Batch size comparison
* Fine-tuning
* Hyperparameter optimization

### Phase 6 – Model Evaluation

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC
* Confusion Matrix

# 🌐 Flask Application Modules

## Home

Project overview and navigation.

## Dashboard

* Dataset summary
* Model summary
* Dataset statistics
* Quick navigation

## Upload

* Upload skin lesion image
* Validate image format

## Prediction

* Predicted disease
* Confidence score
* Class probabilities

## Explainable AI

* Grad-CAM heatmap
* Original image comparison

## Analytics

* Model performance metrics
* Accuracy comparison
* Confusion matrix
* ROC curve
* Performance visualization

## Reports

* Diagnosis Report
* Model Comparison Report

---

# 📈 Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC
* Confusion Matrix
* Precision–Recall Curve

---

# ▶️ Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project directory

```bash
cd Skin Disease Classification & Diagnosis Platform
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

Open your browser

```text
http://127.0.0.1:5000
```

---

# 📷 Application Workflow

1. Open the application.
2. Upload a skin lesion image.
3. The model preprocesses the image.
4. AI predicts the disease class.
5. Confidence scores are displayed.
6. Grad-CAM highlights the important region.
7. View analytics.
8. Download diagnosis and model comparison reports.


# 👨‍💻 Author

**Logesh**