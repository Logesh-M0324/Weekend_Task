import cv2
import numpy as np
import tensorflow as tf


def generate_gradcam(model, image, last_conv_layer_name=None):

    # Convert image to TensorFlow tensor
    image = tf.convert_to_tensor( image, dtype=tf.float32 )

    # Find the last Conv2D layer automatically
    if last_conv_layer_name is None:

        for layer in reversed(model.layers):

            if isinstance(
                layer,  
                tf.keras.layers.Conv2D
            ):
                last_conv_layer_name = layer.name
                break

        if last_conv_layer_name is None:
            raise ValueError(
                "No Conv2D layer was found."
            )

    print(
        "Grad-CAM layer:",
        last_conv_layer_name
    )

    # ------------------------------------------------
    # Create a new Functional model
    # ------------------------------------------------

    inputs = tf.keras.Input(
        shape=(224, 224, 3)
    )

    x = inputs

    last_conv_output = None

    for layer in model.layers:

        x = layer(x)

        if layer.name == last_conv_layer_name:

            last_conv_output = x

    if last_conv_output is None:

        raise ValueError(
            f"Layer '{last_conv_layer_name}' "
            "was not found."
        )

    # This model returns:
    # 1. Last Conv2D feature maps
    # 2. Final class probabilities
    grad_model = tf.keras.Model(
        inputs=inputs,
        outputs=[
            last_conv_output,
            x
        ]
    )

    # ------------------------------------------------
    # Calculate gradients
    # ------------------------------------------------

    with tf.GradientTape() as tape:

        conv_outputs, predictions = grad_model(
            image,
            training=False
        )

        predicted_class = tf.argmax(
            predictions[0]
        )

        class_score = predictions[
            0,
            predicted_class
        ]

    gradients = tape.gradient(
        class_score,
        conv_outputs
    )

    if gradients is None:

        raise ValueError(
            "Grad-CAM gradients are None. "
            "The convolution output is not "
            "connected to the prediction."
        )

    # Average gradients over image height and width
    pooled_gradients = tf.reduce_mean(
        gradients,
        axis=(0, 1, 2)
    )

    # Remove batch dimension
    conv_outputs = conv_outputs[0]

    # Multiply feature maps by their importance
    # weights and add them
    heatmap = tf.reduce_sum(
        conv_outputs * pooled_gradients,
        axis=-1
    )

    # Keep only positive values
    heatmap = tf.maximum(
        heatmap,
        0
    )

    # Normalize between 0 and 1
    maximum = tf.reduce_max(
        heatmap
    )

    heatmap = heatmap / (
        maximum +
        tf.keras.backend.epsilon()
    )

    return heatmap.numpy()


def save_gradcam(
    image_path,
    heatmap,
    output_path
):

    # Read original image
    image = cv2.imread(
        image_path
    )

    if image is None:

        raise ValueError(f"Could not read image: "f"{image_path}")

    image = cv2.resize( image, (224, 224) )

    heatmap = cv2.resize( heatmap, (224, 224) )

    heatmap = np.uint8( 255 * heatmap )

    heatmap = cv2.applyColorMap( heatmap, cv2.COLORMAP_JET )

    superimposed = cv2.addWeighted( image, 0.6, heatmap, 0.4, 0 )

    cv2.imwrite( output_path,superimposed )


def get_last_conv_layer(model):

    for layer in reversed(model.layers):

        if isinstance(
            layer,
            tf.keras.layers.Conv2D
        ):
            return layer.name

    raise ValueError(
        "No Conv2D layer found."
    )