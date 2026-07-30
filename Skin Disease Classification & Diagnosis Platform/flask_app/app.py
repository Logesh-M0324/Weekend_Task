import os

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    flash
)

from werkzeug.utils import secure_filename
from utils.preprocess import preprocess_image
from utils.predict import predict_image

from utils.gradcam import (
    generate_gradcam,
    save_gradcam,
    get_last_conv_layer
)



from utils.predict import model

app = Flask(__name__)

app.secret_key = "my_secret_key"

UPLOAD_FOLDER = "static/uploads"

ALLOWED_EXTENSIONS = {
    "jpg",
    "jpeg",
    "png"
}



app.config["UPLOAD_FOLDER"] = os.path.join("static", "uploads")
app.config["GRADCAM_FOLDER"] = os.path.join("static", "gradcam")

os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
os.makedirs(app.config["GRADCAM_FOLDER"], exist_ok=True)

def allowed_file(filename):

    return (
        "." in filename
        and
        filename.rsplit(".", 1)[1].lower()
        in ALLOWED_EXTENSIONS
    )


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "POST":

        image = request.files.get("image")

        # No file uploaded
        if image is None:
            flash("No file was uploaded.")
            return redirect(request.url)

        # Empty filename
        if image.filename == "":
            flash("Please select an image.")
            return redirect(request.url)

        # Invalid extension
        if not allowed_file(image.filename):
            flash("Only JPG, JPEG and PNG files are allowed.")
            return redirect(request.url)

        # Secure filename
        filename = secure_filename(image.filename)

        # -----------------------------------
        # Save uploaded image
        # -----------------------------------

        save_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        image.save(save_path)

        # -----------------------------------
        # Image preprocessing
        # -----------------------------------

        processed_image = preprocess_image(
            save_path
        )

        # -----------------------------------
        # Prediction
        # -----------------------------------

        predicted_class, confidence, probability_data = predict_image(
            processed_image
        )

        # -----------------------------------
        # Grad-CAM
        # -----------------------------------

        last_conv_layer = get_last_conv_layer(
            model
        )

        heatmap = generate_gradcam(
            model=model,
            image=processed_image,
            last_conv_layer_name=last_conv_layer
        )

        # -----------------------------------
        # Save Grad-CAM image
        # -----------------------------------

        gradcam_filename = f"gradcam_{filename}"

        gradcam_save_path = os.path.join(
            app.config["GRADCAM_FOLDER"],
            gradcam_filename
        )

        save_gradcam(
            save_path,
            heatmap,
            gradcam_save_path
        )

        # -----------------------------------
        # Paths used inside HTML
        # -----------------------------------

        image_path = f"uploads/{filename}"

        gradcam_path = f"gradcam/{gradcam_filename}"
        
        # -----------------------------------
        # Result page
        # -----------------------------------   

        print("=================================================================")

        print(image_path)
        print(gradcam_path)

        print("=================================================================")

        return render_template(
            "result.html",
            image_path=image_path,
            gradcam_path=gradcam_path,
            predicted_class=predicted_class,
            confidence=confidence,
            probability_data=probability_data
        )

    return render_template("upload.html")


@app.route("/dashboard")
def dashboard():

    return render_template(
        "dashboard.html",

        total_images=10015,

        total_classes=7,

        best_model="EfficientNetB0",

        train_count=7000,

        validation_count=1500,

        test_count=1515
    )


@app.route("/analytics")
def analytics():

    return render_template(
        "analytics.html"
    )


if __name__ == "__main__":
    app.run(debug=True)