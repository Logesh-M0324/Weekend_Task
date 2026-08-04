import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.utils.class_weight import compute_class_weight

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import BatchNormalization

from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications import DenseNet121


train_df = pd.read_csv("../Dataset/train_metadata.csv")
valid_df = pd.read_csv("../Dataset/valid_metadata.csv")
test_df = pd.read_csv("../Dataset/test_metadata.csv")

label_encoder = LabelEncoder()

train_df["label"] = label_encoder.fit_transform(train_df["dx"])
valid_df["label"] = label_encoder.transform(valid_df["dx"])
test_df["label"] = label_encoder.transform(test_df["dx"])


NUM_CLASSES = len(label_encoder.classes_)

class_weights = compute_class_weight(
    class_weight="balanced",
    classes=np.unique(train_df["label"]),
    y=train_df["label"]
)

class_weights = dict(enumerate(class_weights))

IMG_SIZE = (224,224)

def process_image(path,label):

    image = tf.io.read_file(path)
    image = tf.image.decode_jpeg(image,channels=3)

    image = tf.image.resize(image,IMG_SIZE)

    image = tf.cast(image,tf.float32)/255.0

    return image,label

data_augmentation = tf.keras.Sequential([

    tf.keras.layers.RandomFlip("horizontal"),

    tf.keras.layers.RandomRotation(0.2),

    tf.keras.layers.RandomZoom(0.2),

    tf.keras.layers.RandomContrast(0.2),

    tf.keras.layers.RandomBrightness(0.2)

])

train_dataset = tf.data.Dataset.from_tensor_slices(
    (train_df["path"], train_df["label"])
)

train_dataset = train_dataset.map(
    process_image,
    num_parallel_calls=tf.data.AUTOTUNE
)

train_dataset = train_dataset.map(
    lambda x, y: (data_augmentation(x, training=True), y),
    num_parallel_calls=tf.data.AUTOTUNE
)

valid_dataset = tf.data.Dataset.from_tensor_slices(
    (valid_df["path"], valid_df["label"])
)

valid_dataset = valid_dataset.map(
    process_image,
    num_parallel_calls=tf.data.AUTOTUNE
)

test_dataset = tf.data.Dataset.from_tensor_slices(
    (test_df["path"], test_df["label"])
)

test_dataset = test_dataset.map(
    process_image,
    num_parallel_calls=tf.data.AUTOTUNE
)

BATCH_SIZE = 32

train_dataset = train_dataset.batch(BATCH_SIZE)
valid_dataset = valid_dataset.batch(BATCH_SIZE)
test_dataset = test_dataset.batch(BATCH_SIZE)

train_dataset = train_dataset.prefetch(tf.data.AUTOTUNE)
valid_dataset = valid_dataset.prefetch(tf.data.AUTOTUNE)
test_dataset = test_dataset.prefetch(tf.data.AUTOTUNE)

basic_cnn = tf.keras.Sequential([

    tf.keras.layers.Input(shape=(224, 224, 3)),

    tf.keras.layers.Conv2D(
        filters=32,
        kernel_size=(3,3),
        activation="relu"
    ),

    tf.keras.layers.MaxPooling2D(pool_size=(2,2)),

    tf.keras.layers.Conv2D(
        filters=64,
        kernel_size=(3,3),
        activation="relu"
    ),

    tf.keras.layers.MaxPooling2D(pool_size=(2,2)),

    tf.keras.layers.Flatten(),

    tf.keras.layers.Dense(
        128,
        activation="relu"
    ),

    tf.keras.layers.Dense(
        NUM_CLASSES,
        activation="softmax"
    )

])  

basic_cnn.compile(

    optimizer="adam",

    loss="sparse_categorical_crossentropy",

    metrics=["accuracy"]

)

history_basic = basic_cnn.fit(

    train_dataset,

    validation_data=valid_dataset,

    epochs=10,

    class_weight=class_weights,

    verbose=1

)