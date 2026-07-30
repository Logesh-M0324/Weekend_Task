import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model("models/best_model.keras")

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