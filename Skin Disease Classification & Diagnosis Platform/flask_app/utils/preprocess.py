import cv2
import numpy as np


IMAGE_SIZE = (224, 224)


def preprocess_image(image_path):
    """
    Reads an image from disk and prepares it
    for TensorFlow prediction.
    """

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Unable to read image.")

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image = cv2.resize(image, IMAGE_SIZE)

    image = image.astype("float32") / 255.0

    image = np.expand_dims(image, axis=0)

    return image