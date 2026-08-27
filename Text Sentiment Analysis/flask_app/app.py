from flask import (
    Flask,
    render_template,
    request,
    send_file
)

import os
import pickle
import numpy as np
import pandas as pd
import tensorflow as tf

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)


app = Flask(__name__)


# --------------------------------------------------
# Configuration
# --------------------------------------------------

UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# --------------------------------------------------
# Load TF-IDF Vectorizer
# --------------------------------------------------

with open(
    "data/processed/tfidf_vectorizer.pkl",
    "rb"
) as file:

    tfidf_vectorizer = pickle.load(file)


# --------------------------------------------------
# Load Best ANN Model
# --------------------------------------------------

ann_model = tf.keras.models.load_model(
    "../models/ann/ann_baseline.keras"
)


# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

dataset = pd.read_csv(
    "../Dataset/IMDB Dataset.csv"
)


# --------------------------------------------------
# Dataset Statistics
# --------------------------------------------------

total_reviews = len(dataset)

positive_reviews = (
    dataset["sentiment"]
    .str.lower()
    .eq("positive")
    .sum()
)

negative_reviews = (
    dataset["sentiment"]
    .str.lower()
    .eq("negative")
    .sum()
)


# --------------------------------------------------
# Home Dashboard
# --------------------------------------------------

@app.route("/")
def index():

    dataset_stats = {
        "total_reviews": total_reviews,
        "positive_reviews": positive_reviews,
        "negative_reviews": negative_reviews
    }

    model_summary = {
        "model": "Optimized ANN",
        "accuracy": 0.904679,
        "precision": 0.904494,
        "recall": 0.905706,
        "f1": 0.905100,
        "roc_auc": 0.967430
    }

    return render_template(
        "index.html",
        dataset_stats=dataset_stats,
        model_summary=model_summary
    )


# --------------------------------------------------
# Text Preprocessing for ANN
# --------------------------------------------------

def preprocess_text(text):

    text = str(text)

    text = text.lower()

    return text


# --------------------------------------------------
# Single Review Prediction
# --------------------------------------------------

@app.route("/predict", methods=["GET", "POST"])
def predict():

    prediction = None
    probabilities = None
    review = ""

    if request.method == "POST":

        review = request.form.get(
            "review",
            ""
        )

        if review.strip():

            cleaned_review = preprocess_text(
                review
            )

            review_tfidf = (
                tfidf_vectorizer.transform(
                    [cleaned_review]
                )
            )

            probability = ann_model.predict(
                review_tfidf,
                verbose=0
            )[0][0]

            positive_probability = (
                float(probability) * 100
            )

            negative_probability = (
                (1 - float(probability)) * 100
            )

            if probability >= 0.5:

                prediction = "Positive"

            else:

                prediction = "Negative"

            probabilities = {
                "positive": round(
                    positive_probability,
                    2
                ),
                "negative": round(
                    negative_probability,
                    2
                )
            }

    return render_template(
        "predict.html",
        prediction=prediction,
        probabilities=probabilities,
        review=review
    )


# --------------------------------------------------
# Model Comparison
# --------------------------------------------------

@app.route("/comparison")
def comparison():

    comparison_data = [
        {
            "model": "ANN",
            "accuracy": 0.904679,
            "precision": 0.904494,
            "recall": 0.905706,
            "f1": 0.905100,
            "roc_auc": 0.967430
        },

        {
            "model": "RNN",
            "accuracy": 0.4977,
            "precision": 0.0,
            "recall": 0.0,
            "f1": 0.0,
            "roc_auc": 0.5000
        },

        {
            "model": "LSTM",
            "accuracy": 0.8653,
            "precision": 0.0,
            "recall": 0.0,
            "f1": 0.0,
            "roc_auc": 0.9321
        },

        {
            "model": "GRU",
            "accuracy": 0.8721,
            "precision": 0.0,
            "recall": 0.0,
            "f1": 0.0,
            "roc_auc": 0.9353
        },

        {
            "model": "Bi-LSTM",
            "accuracy": 0.8643,
            "precision": 0.0,
            "recall": 0.0,
            "f1": 0.0,
            "roc_auc": 0.9358
        }
    ]

    return render_template(
        "comparison.html",
        comparison_data=comparison_data
    )


# --------------------------------------------------
# Text Analytics
# --------------------------------------------------

@app.route("/analytics")
def analytics():

    sentiment_counts = (
        dataset["sentiment"]
        .value_counts()
        .to_dict()
    )

    dataset["review_length"] = (
        dataset["review"]
        .astype(str)
        .str.split()
        .str.len()
    )

    average_length = round(
        dataset["review_length"].mean(),
        2
    )

    return render_template(
        "analytics.html",
        sentiment_counts=sentiment_counts,
        average_length=average_length
    )


# --------------------------------------------------
# Batch Prediction
# --------------------------------------------------

@app.route("/batch", methods=["GET", "POST"])
def batch():

    result_file = None
    prediction_summary = None

    if request.method == "POST":

        file = request.files.get("file")

        if file and file.filename.endswith(".csv"):

            input_path = os.path.join(
                app.config["UPLOAD_FOLDER"],
                file.filename
            )

            file.save(input_path)

            batch_data = pd.read_csv(
                input_path
            )

            if "review" not in batch_data.columns:

                return render_template(
                    "batch.html",
                    error="CSV must contain a 'review' column."
                )

            cleaned_reviews = (
                batch_data["review"]
                .astype(str)
                .apply(preprocess_text)
                .tolist()
            )

            tfidf_data = (
                tfidf_vectorizer.transform(
                    cleaned_reviews
                )
            )

            probabilities = (
                ann_model.predict(
                    tfidf_data,
                    verbose=0
                ).ravel()
            )

            predictions = np.where(
                probabilities >= 0.5,
                "Positive",
                "Negative"
            )

            batch_data["sentiment"] = predictions

            batch_data["confidence"] = np.maximum(
                probabilities,
                1 - probabilities
            )

            result_path = os.path.join(
                RESULT_FOLDER,
                "sentiment_predictions.csv"
            )

            batch_data.to_csv(
                result_path,
                index=False
            )

            prediction_summary = (
                batch_data["sentiment"]
                .value_counts()
                .to_dict()
            )

            result_file = "sentiment_predictions.csv"

    return render_template(
        "batch.html",
        result_file=result_file,
        prediction_summary=prediction_summary
    )


# --------------------------------------------------
# Download Batch Results
# --------------------------------------------------

@app.route("/download/<filename>")
def download(filename):

    file_path = os.path.join(
        RESULT_FOLDER,
        filename
    )

    return send_file(
        file_path,
        as_attachment=True
    )


# --------------------------------------------------
# Run Application
# --------------------------------------------------

if __name__ == "__main__":

    app.run(
        debug=True
    )