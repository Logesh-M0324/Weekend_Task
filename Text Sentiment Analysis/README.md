# End-to-End Text Sentiment Analysis using RNN, LSTM, GRU and TensorFlow

An end-to-end deep learning project for classifying IMDb movie reviews into sentiment categories using TensorFlow/Keras. The project covers the complete machine learning lifecycle, from data understanding and text preprocessing to model development, optimization, evaluation, interpretation, and deployment using Flask.

--- 

## Project Overview

Sentiment analysis is a Natural Language Processing (NLP) task used to determine the emotional orientation of a piece of text.

In this project, the IMDb Movie Reviews dataset is used to build a deep learning-based sentiment analysis system.

The system analyzes a movie review and predicts whether the review expresses:

- **Positive sentiment**
- **Negative sentiment**

Multiple neural network architectures are developed and compared:

- Artificial Neural Network (ANN)
- Simple RNN
- LSTM
- GRU
- Bidirectional LSTM (Bi-LSTM)

The final trained model is integrated into an interactive Flask web application where users can enter individual reviews or upload a CSV file for batch sentiment prediction.

---

## Project Objectives

The main objectives of this project are:

1. Understand and analyze the IMDb movie review dataset.
2. Perform text cleaning and preprocessing.
3. Convert textual data into machine-readable representations.
4. Establish a TF-IDF baseline.
5. Build ANN, RNN, LSTM, GRU and Bi-LSTM models.
6. Compare the performance of different architectures.
7. Improve the models through controlled experiments.
8. Evaluate the models using multiple classification metrics.
9. Analyze model predictions and misclassified reviews.
10. Select the best-performing model.
11. Deploy the trained model through a Flask web application.
12. Implement single-review and batch prediction functionality.
13. Maintain the complete project using Git and GitHub.

---

# Dataset

## IMDb Movie Reviews Dataset

The project uses the **IMDb Dataset of 50K Movie Reviews**.

Dataset source:

https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

### Dataset Features

| Feature | Description |
|---|---|
| `review` | Movie review text |
| `sentiment` | Sentiment label |

The dataset contains approximately **50,000 movie reviews**, consisting of positive and negative reviews.

---

# Project Workflow

The project is implemented in eight major phases.

```text
                 IMDb 50K Dataset
                        │
                        ▼
              Phase 1: Data Understanding
                        │
                        ▼
              Phase 2: Text Preprocessing
                        │
                        ▼
              Phase 3: Feature Representation
                        │
             ┌──────────┴──────────┐
             │                     │
           TF-IDF             Token Encoding
             │                     │
             │              Trainable Embedding
             │                     │
             └──────────┬──────────┘
                        ▼
              Phase 4: Model Development
                        │
          ┌─────────────┼─────────────┐
          │             │             │
         ANN           RNN           LSTM
          │             │             │
          └─────────────┼─────────────┘
                        │
                  GRU / Bi-LSTM
                        │
                        ▼
              Phase 5: Optimization
                        │
                        ▼
              Phase 6: Evaluation
                        │
                        ▼
              Phase 7: Model Comparison
                        │
                        ▼
              Phase 8: Interpretation
                        │
                        ▼
                Flask Web Application
                        │
             ┌──────────┴──────────┐
             │                     │
       Single Prediction      Batch Prediction
```

## Phase 1 – Data Understanding

The first phase focused on understanding the structure and characteristics of the IMDb dataset.

Tasks Completed
Loaded the IMDb dataset.
Examined the dataset structure.
Checked data types.
Checked missing values.
Checked duplicate reviews.
Analyzed positive and negative sentiment distribution.
Analyzed review length.
Explored frequently occurring words.
Generated visualizations.
Exploratory Visualizations

The following visualizations were created:

Sentiment Distribution
Review Length Distribution
Word Frequency
Word Cloud

These visualizations helped understand the overall distribution of the dataset and the language patterns associated with different sentiments.

## Phase 2 – Text Preprocessing

Raw review text cannot be directly provided to a neural network. Therefore, a preprocessing pipeline was created.

Preprocessing Steps

The preprocessing pipeline includes:

Convert text to lowercase.
Remove HTML tags.
Remove unnecessary characters.
Remove punctuation where appropriate.
Handle stopwords.
Tokenize the reviews.
Convert words into integer sequences.
Apply padding.
Create training, validation and test datasets.

An important consideration during preprocessing is the treatment of sentiment-related words such as:

not
no
never
neither
nor

These words can significantly change the meaning of a review and therefore should not be blindly removed during sentiment preprocessing.

For example:

The movie is good.

and

The movie is not good.

express different sentiments.

The preprocessing pipeline therefore preserves important negation information.

## Phase 3 – Feature Representation

Different methods of representing text were investigated.

#### 1. Integer Encoding

Words are converted into integer IDs using tokenization.

Example:

movie → 25
good  → 48
amazing → 91

A review is therefore represented as a sequence of integers.

#### 2. TF-IDF

TF-IDF was implemented as a traditional machine-learning baseline.

TF-IDF represents a word based on:

Its frequency within a document.
Its importance across the complete collection of documents.

The TF-IDF representation was used as a baseline representation rather than as the input representation for the recurrent neural network architectures.

#### 3. Trainable Word Embeddings

For the deep learning sequence models, a trainable embedding layer was used.

The embedding layer learns a dense vector representation of words during model training.

The general pipeline is:

Text
  ↓
Tokenization
  ↓
Integer Sequences
  ↓
Padding
  ↓
Embedding Layer
  ↓
Neural Network

## Phase 4 – Deep Learning Models

Multiple neural network architectures were developed using TensorFlow/Keras.

### Models Implemented

#### 1. Artificial Neural Network (ANN)

The ANN provides a feed-forward neural network baseline.

General structure:

Input
  ↓
Dense Layer
  ↓
Activation
  ↓
Dropout
  ↓
Dense Layer
  ↓
Output

#### 2. Simple RNN

The Simple RNN processes the review sequentially and maintains information from previous words.

Input Sequence
      ↓
   Embedding
      ↓
   Simple RNN
      ↓
     Dense
      ↓
    Output

#### 3. LSTM

Long Short-Term Memory networks were implemented to handle long-term dependencies more effectively than a basic RNN.

Input Sequence
      ↓
   Embedding
      ↓
     LSTM
      ↓
     Dense
      ↓
    Output

#### 4. GRU

The Gated Recurrent Unit provides a simpler recurrent architecture while maintaining the ability to capture sequential dependencies.

Input Sequence
      ↓
  Embedding
      ↓
     GRU
      ↓
    Dense
      ↓
   Output

#### 5. Bidirectional LSTM

The Bi-LSTM processes the sequence in both forward and backward directions.

                 ┌── Forward LSTM ──┐
Input Sequence ──┤                  ├── Output
                 └─ Backward LSTM ──┘

This allows the model to use contextual information from both directions.

##### Phase 5 – Model Improvement

After establishing baseline models, multiple enhancement experiments were performed.

The purpose of this phase was to investigate how different hyperparameters and regularization techniques affect model performance.

Optimization Techniques

The experiments included:

Dropout = 0.3
Dropout = 0.5
Batch Normalization
RMSprop optimizer
Learning-rate tuning
Batch-size tuning
Hidden-unit tuning
Sequence-length tuning
Early Stopping
Learning-rate scheduling

The enhancements were evaluated separately for the appropriate model architectures.

Why Optimization Was Performed Separately

Different architectures have different characteristics.

For example:

ANN does not use recurrent layers.
RNN, LSTM, GRU and Bi-LSTM process sequential information.
Embedding layers are used with sequence-based deep learning models.
TF-IDF is primarily used as a traditional feature representation/baseline rather than being directly combined with the recurrent architectures.

Therefore, each enhancement was applied according to the architecture being optimized.

#### Phase 6 – Model Evaluation

The trained models were evaluated using multiple classification metrics.

Evaluation Metrics
Accuracy

Measures the proportion of correctly classified reviews.

Accuracy =
Correct Predictions / Total Predictions
Precision

Measures how many reviews predicted as a particular class were actually members of that class.

Precision =
TP / (TP + FP)
Recall

Measures how many actual samples of a class were correctly identified.

Recall =
TP / (TP + FN)
F1 Score

The F1 score combines precision and recall.

F1 =
2 × Precision × Recall
/
(Precision + Recall)
ROC-AUC

ROC-AUC measures the model's ability to distinguish between the sentiment classes across different classification thresholds.

Visualizations

The evaluation phase includes:

Training vs Validation Accuracy
Training vs Validation Loss
Confusion Matrix
ROC Curve
Precision-Recall Curve
Misclassified Reviews

These visualizations provide a more detailed understanding of model behavior beyond accuracy alone.

#### Phase 7 – Model Comparison

The performance of the different models was compared using:

Model	    Accuracy	Precision	Recall	F1 Score	ROC-AUC
ANN	    90.47%   	90.45%	90.57%	90.51%	96.74%
RNN	    52.32%	      67.34%	9.72%	      16.99%      53.87%
LSTM	    87.67%	      88.32%	86.92%	87.61%      94.43%
GRU	    89.17%	      88.34%	90.35%	89.33%	95.93%
Bi-LSTM   87.34%	      87.75%	86.90%	87.32%	93.00%

Note: Replace the remaining values with the final confirmed Phase 7 results from the completed experiment table.

Best Model Selection

The final model was selected by considering:

Validation performance
Test accuracy
Precision
Recall
F1 Score
ROC-AUC
Generalization performance

The final selected model is used by the Flask application for sentiment prediction.

#### Phase 8 – Model Interpretation

The final phase focused on understanding the model predictions rather than only measuring numerical performance.

Analysis Performed
Important Words

The project investigates words and language patterns that are strongly associated with positive and negative sentiment.

#### Correctly Classified Reviews

Examples of reviews that were correctly classified were examined to understand the language patterns learned by the model.

Misclassified Reviews

Misclassified reviews were analyzed to identify difficult cases.

Possible reasons include:

Sarcasm
Ambiguous language
Mixed opinions
Negation
Very short reviews
Complex sentence structure
Context-dependent expressions
Model Limitations

The model may have difficulty with reviews containing:

Sarcasm
Multiple opposing opinions
Unusual expressions
Context that depends on external knowledge
Words whose sentiment depends heavily on sentence context
Flask Web Application

A Flask-based web application was developed to make the trained sentiment analysis model accessible through an interactive interface.

### The application provides several sections.

#### 1. Dashboard

The dashboard provides:

Project overview
Dataset statistics
Number of reviews
Positive review count
Negative review count
Best model information
Model performance summary

#### 2. Sentiment Prediction

Users can enter or paste a movie review.

Example:

This movie was absolutely amazing. The acting and story were excellent.

The application processes the review and displays:

Predicted sentiment
Confidence
Positive probability
Negative probability

Example:

Prediction: POSITIVE

Positive: 94.82%
Negative: 5.18%

#### 3. Model Comparison

The Model Comparison page displays the performance of the developed models.

Metrics include:

Accuracy
Precision
Recall
F1 Score
ROC-AUC

The page also provides model-related evaluation visualizations.

#### 4. Text Analytics

The analytics section presents visual information from the dataset, including:

Sentiment distribution
Review length analysis
Word frequency
Word cloud

#### 5. Batch Prediction

Users can upload a CSV file containing reviews.

The application:

CSV Upload
    ↓
Read Reviews
    ↓
Preprocess Text
    ↓
Tokenize
    ↓
Pad Sequences
    ↓
Load Trained Model
    ↓
Generate Predictions
    ↓
Display Results
    ↓
Download CSV

The generated output contains the predicted sentiment for each review.

## Application Architecture

                    Browser
                       │
                       ▼
                 Flask Application
                       │
             ┌─────────┴─────────┐
             │                   │
          Routes              Templates
             │                   │
             ▼                   ▼
       Prediction Logic      Bootstrap UI
             │
             ▼
       Text Preprocessing
             │
             ▼
       Tokenizer / Encoder
             │
             ▼
        Trained Model
             │
             ▼
        Sentiment Result
Project Structure

The project is organized into separate directories for data, notebooks, models, preprocessing, Flask application and documentation.

IMDb-Sentiment-Analysis/
│
├── data/
│   ├── raw/
│   │   └── IMDB Dataset.csv
│   │
│   └── processed/
│
│
├── notebooks/
│   │
│   ├── phase_1_data_understanding.ipynb
│   ├── phase_2_text_preprocessing.ipynb
│   ├── phase_3_feature_representation.ipynb
│   ├── phase_4_deep_learning_models.ipynb
│   ├── phase_5_model_optimization.ipynb
│   ├── phase_6_model_evaluation.ipynb
│   ├── phase_7_model_comparison.ipynb
│   └── phase_8_model_interpretation.ipynb
│
│
├── models/
│   ├── ann/
│   ├── rnn/
│   ├── lstm/
│   ├── gru/
│   └── bi_lstm/
│
│
├── preprocessing/
│   ├── text_cleaning.py
│   └── preprocessing_pipeline.py
│
│
├── flask_app/
│   │
│   ├── app.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── predict.html
│   │   ├── comparison.html
│   │   ├── analytics.html
│   │   └── batch.html
│   │
│   └── static/
│       ├── css/
│       │   └── style.css
│       │
│       ├── js/
│       │
│       └── images/
│
│
├── reports/
│
├── requirements.txt
│
├── .gitignore
│
└── README.md

The exact directory names may differ slightly depending on the final local project structure.

#### Technologies Used

Technology	Purpose
Python	Programming language
Pandas	Data manipulation
NumPy	Numerical operations
TensorFlow	Deep learning
Keras	Neural network development
Scikit-learn	TF-IDF and evaluation
NLTK	Text preprocessing
Matplotlib	Visualization
Seaborn	Statistical visualization
Flask	Web application
Bootstrap	Frontend design
HTML/CSS	Web interface
Git	Version control

#### GitHub	Repository hosting

Installation
1. Clone the Repository
git clone <YOUR_GITHUB_REPOSITORY_URL>

Move into the project directory:

cd IMDb-Sentiment-Analysis
2. Create a Virtual Environment
Windows
pipenv install

and go to the project directory then,
Activate:
pipenv shell

3. Running the Flask Application

Navigate to the Flask application directory:

cd flask_app

Run:

python app.py

The Flask development server will start.

Open the local address shown by Flask in your browser.

Example Prediction

Input:

The movie was fantastic. The story was interesting and the performances were excellent.

Expected output:

Sentiment: Positive

Another example:

The movie was boring and disappointing. I would not recommend it.

Expected output:

Sentiment: Negative

The application also displays the class probabilities.

Batch Prediction

The batch prediction feature accepts a CSV file containing a review column.

#### Example:

review
"This movie was excellent and enjoyable"
"The story was boring and disappointing"
"An amazing performance by the entire cast"

After uploading the file, the application generates predictions.

Example output:

review,predicted_sentiment
"This movie was excellent and enjoyable",positive
"The story was boring and disappointing",negative
"An amazing performance by the entire cast",positive

The generated results can be downloaded from the application.

Model Saving

The trained models are saved so that they can be reused by the Flask application without retraining.

The application loads the selected final model during prediction.

This separates:

Model Training

from:

Model Deployment

and avoids unnecessary retraining every time the Flask application starts.

Git and GitHub

Git was used to maintain the project source code and experiment history.

The repository contains:

Jupyter notebooks
Preprocessing code
Model code
Flask application
Frontend templates
CSS
Documentation
Requirements
Git configuration

Meaningful commits were used to track major stages of development.

#### Example:

git add .
git commit -m "Complete Phase 1 data understanding"
git add .
git commit -m "Complete text preprocessing pipeline"
git add .
git commit -m "Add deep learning sentiment models"
git add .
git commit -m "Complete model optimization experiments"
git add .
git commit -m "Add Flask sentiment prediction application"
requirements.txt

The project dependencies include the major libraries required for preprocessing, model development, evaluation and deployment.

#### Example:

numpy
pandas
tensorflow
scikit-learn
nltk
matplotlib
seaborn
flask

Additional packages used by the final application should also be included in the project's requirements.txt.

.gitignore

The .gitignore file prevents unnecessary files from being committed to GitHub.

Typical entries include:

venv/
__pycache__/
*.pyc
.ipynb_checkpoints/
.env
.DS_Store

Large datasets and unnecessary generated files should also be excluded when appropriate.

Key Features
IMDb 50K movie review dataset
Complete NLP preprocessing pipeline
Negation-aware text preprocessing
Integer sequence representation
TF-IDF baseline
Trainable word embeddings
ANN model
Simple RNN model
LSTM model
GRU model
Bidirectional LSTM model
Hyperparameter optimization
Multiple evaluation metrics
Confusion matrix
ROC curve
Precision-Recall curve
Misclassified review analysis
Model comparison
Interactive Flask dashboard
Single-review prediction
Probability/confidence display
Batch CSV prediction
Downloadable prediction results
Responsive Bootstrap interface
Git/GitHub version control
Results

The project demonstrated that deep learning models can effectively classify movie reviews based on their textual content.

The final comparison considers both predictive performance and generalization rather than relying only on training accuracy.

The optimized model selected during Phase 7 is used for the final Flask deployment.

Final Model
Selected Model: <ENTER FINAL MODEL>
Accuracy:       <ENTER FINAL ACCURACY>
Precision:      <ENTER FINAL PRECISION>
Recall:         <ENTER FINAL RECALL>
F1 Score:       <ENTER FINAL F1 SCORE>
ROC-AUC:        <ENTER FINAL ROC-AUC>

Replace the values above with the final confirmed Phase 7 results.

## Limitations

Although the system performs well on the IMDb dataset, it has several limitations.

#### Dataset Limitation

The model is trained specifically on movie reviews and may not perform equally well on other domains such as:

Product reviews
Customer service messages
Social media posts
News comments
Sarcasm

Sarcastic statements can be difficult to classify because the literal words may have a different sentiment from the intended meaning.

#### Context

Some reviews require broader context to correctly determine sentiment.


## Conclusion

This project developed a complete end-to-end sentiment analysis system using the IMDb 50K movie review dataset. The workflow covered data understanding, text preprocessing, feature representation, neural network development, optimization, evaluation, model comparison and interpretation. ANN, RNN, LSTM, GRU and Bi-LSTM architectures were implemented and evaluated using multiple classification metrics. Finally, the selected model was integrated into a Flask web application supporting single-review prediction, probability analysis, model comparison, text analytics and batch CSV prediction. The project demonstrates the complete process of taking an NLP problem from raw text data to a deployable deep learning application.