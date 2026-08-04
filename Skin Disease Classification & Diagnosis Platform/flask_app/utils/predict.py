import numpy as np
import tensorflow as tf
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "models", "best_model.keras")  # Adjust "models" if folder name differs

model = tf.keras.models.load_model(MODEL_PATH)

CLASS_NAMES = [
    "Actinic Keratosis",
    "Basal Cell Carcinoma",
    "Benign Keratosis",
    "Dermatofibroma",
    "Melanoma",
    "Melanocytic Nevus",
    "Vascular Lesion"
]


def predict_image(image):

    predictions = model.predict(image, verbose=0)[0]

    predicted_index = np.argmax(predictions)

    predicted_class = CLASS_NAMES[predicted_index]

    confidence = predictions[predicted_index] * 100

    probability_data = []

    for class_name, probability in zip(CLASS_NAMES, predictions):

        probability_data.append(
            {
                "class_name": class_name,
                "probability": probability * 100
            }
        )

    probability_data.sort(
        key=lambda x: x["probability"],
        reverse=True
    )

    return (
        predicted_class,
        confidence,
        probability_data
    )