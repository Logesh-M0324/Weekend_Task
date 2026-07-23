from flask import Flask, render_template, request
import pickle
import pandas as pd
from flask import send_file

app = Flask(__name__)

with open("../dataset/models/best_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():

    if request.method == "POST":

        overall_qual = int(request.form["OverallQual"])
        garage_cars = int(request.form["GarageCars"])
        garage_area = float(request.form["GarageArea"])
        lot_area = float(request.form["LotArea"])
        mas_vnr_area = float(request.form["MasVnrArea"])

        # Year should be an integer
        garage_yr_blt = int(request.form["GarageYrBlt"])

        fireplaces = int(request.form["Fireplaces"])
        total_rooms = int(request.form["TotRmsAbvGrd"])

        kitchen = request.form["KitchenQual"]
        basement = request.form["BsmtQual"]

        input_data = {
            "OverallQual": overall_qual,
            "GarageCars": garage_cars,
            "GarageArea": garage_area,
            "LotArea": lot_area,
            "MasVnrArea": mas_vnr_area,
            "GarageYrBlt": garage_yr_blt,
            "Fireplaces": fireplaces,
            "TotRmsAbvGrd": total_rooms,

            "KitchenQual_Fa": 0,
            "KitchenQual_Gd": 0,
            "KitchenQual_TA": 0,

            "BsmtQual_Fa": 0,
            "BsmtQual_Gd": 0,
            "BsmtQual_TA": 0
        }

        if kitchen == "Fa":
            input_data["KitchenQual_Fa"] = 1
        elif kitchen == "Gd":
            input_data["KitchenQual_Gd"] = 1
        elif kitchen == "TA":
            input_data["KitchenQual_TA"] = 1

        if basement == "Fa":
            input_data["BsmtQual_Fa"] = 1
        elif basement == "Gd":
            input_data["BsmtQual_Gd"] = 1
        elif basement == "TA":
            input_data["BsmtQual_TA"] = 1

        input_df = pd.DataFrame([input_data])

        prediction = model.predict(input_df)

        predicted_price = round(prediction[0], 2)

        return render_template(
            "result.html",
            prediction=predicted_price
        )

    return render_template("predict.html")


@app.route("/dashboard")
def dashboard():

    return render_template("dashboard.html")

@app.route("/comparison")
def comparison():

    return render_template("comparison.html")

@app.route("/analytics")
def analytics():

    return render_template("analytics.html")

@app.route("/reports")
def reports():

    return render_template("reports.html")

@app.route("/download_prediction_report")
def download_prediction_report():
    return send_file(
        "reports/Prediction_Report.docx",
        as_attachment=True
    )


@app.route("/download_evaluation_report")
def download_evaluation_report():
    return send_file(
        "reports/Evaluation_Report.docx",
        as_attachment=True
    )


@app.route("/download_comparison_report")
def download_comparison_report():
    return send_file(
        "reports/Comparison_Report.docx",
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True)

