import tensorflow as tf
import numpy as np
import joblib
import pandas as pd
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error
)
from flask import Flask, render_template, request


app = Flask(__name__)

model = tf.keras.models.load_model(
    "../Models/bilstm_model_48_RMS_86.keras"
)

X_scaler = joblib.load(
    "../Models/X_scaler.pkl"
)

y_scaler = joblib.load(
    "../Models/y_scaler.pkl"
)


@app.route("/")
def dashboard():

    df = pd.read_csv("../Dataset/final_df.csv")

    df["Datetime"] = pd.to_datetime(df["Datetime"])


    df = df.sort_values("Datetime")

    latest_demand = round(
        df["PJME_MW"].iloc[-1],
        2
    )

    chart_df = df.tail(168)

    dates = chart_df["Datetime"].dt.strftime(
        "%Y-%m-%d %H:%M"
    ).tolist()

    demand = chart_df["PJME_MW"].tolist()

    model_performance = [

        {
            "Model": "Naive",
            "MAE": 1207.85,
            "RMSE": 1808.40,
            "MAPE": 3.859,
            "R2": 0.916
        },

        {
            "Model": "Previous-Day",
            "MAE": 2267.29,
            "RMSE": 3120.64,
            "MAPE": 7.123,
            "R2": 0.749
        },

        {
            "Model": "RNN",
            "MAE": 2505.47,
            "RMSE": 3429.29,
            "MAPE": 8.3724,
            "R2": 0.7188
        },

        {
            "Model": "LSTM",
            "MAE": 3084.03,
            "RMSE": 4103.47,
            "MAPE": 10.45,
            "R2": 0.5973
        },

        {
            "Model": "GRU",
            "MAE": 3431.36,
            "RMSE": 4571.74,
            "MAPE": 11.59,
            "R2": 0.498
        },

        {
            "Model": "Bi-LSTM",
            "MAE": 2483.91,
            "RMSE": 3341.67,
            "MAPE": 8.34,
            "R2": 0.732
        }

    ]


    return render_template(

        "dashboard.html",

        latest_demand=latest_demand,

        best_model="Bi-LSTM",

        dates=dates,

        demand=demand,

        model_performance=model_performance

    )


@app.route("/forecast", methods=["GET", "POST"])
def forecast_page():

    forecast = None
    forecast_dates = None

    horizon = 24

    average_forecast = None
    peak_forecast = None

    if request.method == "POST":

        horizon = int(request.form["horizon"])

        df = pd.read_csv(
            "../Dataset/final_df.csv"
        )

        df["Datetime"] = pd.to_datetime(
            df["Datetime"]
        )

        df = df.sort_values(
            "Datetime"
        ).reset_index(drop=True)


        features = [

            "PJME_MW",

            "Hour",
            "Day",
            "Week",
            "Month",
            "DayOfWeek",
            "IsWeekend",

            "Lag_1",
            "Lag_24",
            "Lag_168",

            "RollingMean_24",
            "RollingMean_168",
            "RollingStd_24",

            "Lag_2",
            "Lag_3",
            "Lag_6",
            "Lag_12",
            "Lag_48",
            "Lag_72"

        ]

        X_scaler = joblib.load(
            "../Models/X_scaler.pkl"
        )

        y_scaler = joblib.load(
            "../Models/y_scaler.pkl"
        )

        sequence_length = 48
        model_horizon = 24
        all_predictions = []
        all_dates = []

        work_df = df[["Datetime", "PJME_MW"]].copy()

        while len(all_predictions) < horizon:

            temp_df = work_df.copy()

            temp_df["Hour"] = (
                temp_df["Datetime"].dt.hour
            )

            temp_df["Day"] = (
                temp_df["Datetime"].dt.day
            )

            temp_df["DayOfWeek"] = (
                temp_df["Datetime"].dt.dayofweek
            )

            temp_df["Week"] = (
                temp_df["Datetime"]
                .dt.isocalendar()
                .week
                .astype(int)
            )

            temp_df["Month"] = (
                temp_df["Datetime"].dt.month
            )

            temp_df["Year"] = (
                temp_df["Datetime"].dt.year
            )

            temp_df["IsWeekend"] = (
                temp_df["DayOfWeek"] >= 5
            ).astype(int)

            temp_df["Lag_1"] = (
                temp_df["PJME_MW"].shift(1)
            )

            temp_df["Lag_2"] = (
                temp_df["PJME_MW"].shift(2)
            )

            temp_df["Lag_3"] = (
                temp_df["PJME_MW"].shift(3)
            )

            temp_df["Lag_6"] = (
                temp_df["PJME_MW"].shift(6)
            )

            temp_df["Lag_12"] = (
                temp_df["PJME_MW"].shift(12)
            )

            temp_df["Lag_24"] = (
                temp_df["PJME_MW"].shift(24)
            )

            temp_df["Lag_48"] = (
                temp_df["PJME_MW"].shift(48)
            )

            temp_df["Lag_72"] = (
                temp_df["PJME_MW"].shift(72)
            )

            temp_df["Lag_168"] = (
                temp_df["PJME_MW"].shift(168)
            )

            temp_df["RollingMean_24"] = (
                temp_df["PJME_MW"]
                .rolling(24)
                .mean()
            )

            temp_df["RollingMean_168"] = (
                temp_df["PJME_MW"]
                .rolling(168)
                .mean()
            )

            temp_df["RollingStd_24"] = (
                temp_df["PJME_MW"]
                .rolling(24)
                .std()
            )

            latest_features = temp_df[
                features
            ].tail(sequence_length)

            if len(latest_features) < sequence_length:

                raise ValueError(
                    "Not enough historical data "
                    "to create the 48-hour sequence."
                )


            latest_features = (
                latest_features
                .bfill()
                .ffill()
            )

            latest_scaled = X_scaler.transform(
                latest_features
            )


            X_input = latest_scaled.reshape(
                1,
                sequence_length,
                len(features)
            )


            print("X_input shape:",X_input.shape)


            prediction_scaled = model.predict(
                X_input,
                verbose=0
            )


            print("Prediction shape:",prediction_scaled.shape)

            prediction = (
                y_scaler
                .inverse_transform(
                    prediction_scaled
                    .reshape(-1, 1)
                )
                .flatten()
            )

            remaining = (
                horizon -
                len(all_predictions)
            )


            take = min(
                model_horizon,
                remaining
            )

            prediction = prediction[:take]


            last_timestamp = (
                work_df["Datetime"].iloc[-1]
            )


            future_dates = pd.date_range(

                start=(
                    last_timestamp
                    + pd.Timedelta(hours=1)
                ),

                periods=take,

                freq="h"

            )

            all_predictions.extend(
                prediction.tolist()
            )

            all_dates.extend(
                future_dates.tolist()
            )


            new_rows = pd.DataFrame({

                "Datetime":
                    future_dates,

                "PJME_MW":
                    prediction

            })


            work_df = pd.concat(

                [
                    work_df,
                    new_rows
                ],

                ignore_index=True

            )


        forecast = [

            round(float(value), 2)

            for value in all_predictions[:horizon]

        ]


        forecast_dates = [

            date.strftime(
                "%Y-%m-%d %H:%M"
            )

            for date in all_dates[:horizon]

        ]

        average_forecast = round(

            float(
                np.mean(forecast)
            ),

            2

        )


        peak_forecast = round(

            float(
                np.max(forecast)
            ),

            2

        )


    return render_template(

        "forecast.html",

        forecast=forecast,

        forecast_dates=forecast_dates,

        horizon=horizon,

        average_forecast=average_forecast,

        peak_forecast=peak_forecast

    )


@app.route("/analytics")
def analytics():

    df = pd.read_csv("../Dataset/final_df.csv")

    df["Datetime"] = pd.to_datetime(df["Datetime"])
    df = df.sort_values("Datetime")

    historical_df = df.tail(30 * 24)
    print("Historical DataFrame:", historical_df.head())
    historical_dates = (
        historical_df["Datetime"]
        .dt.strftime("%Y-%m-%d %H:%M")
        .tolist()
    )
    print("Historical Dates:", historical_dates[:5])

    historical_demand = (
        historical_df["PJME_MW"]
        .round(2)
        .tolist()
    )

    forecast_dates = historical_dates[-24:]
    print("Forecast Dates:", forecast_dates[:5])

    print("Forecast Dates Length:", len(forecast_dates))

    forecast_errors = [1.0] * len(forecast_dates)

    print("Forecast Errors:", forecast_errors[:5])
    return render_template(
        "analytics.html",

        historical_dates=historical_dates,
        historical_demand=historical_demand,

        forecast_dates=forecast_dates,
        forecast_errors=forecast_errors
    )

@app.route("/validation", methods=["GET", "POST"])
def validation():

    # Default validation period
    days = 30

    actual_values = []
    predicted_values = []
    validation_dates = []

    mae = None
    rmse = None
    mape = None

    if request.method == "POST":

        days = int(request.form["days"])


        df = pd.read_csv(
            "../Dataset/final_df.csv"
        )

        df["Datetime"] = pd.to_datetime(
            df["Datetime"]
        )

        df = df.sort_values(
            "Datetime"
        ).reset_index(drop=True)


        features = [

            "PJME_MW",

            "Hour",
            "Day",
            "Week",
            "Month",
            "DayOfWeek",
            "IsWeekend",

            "Lag_1",
            "Lag_24",
            "Lag_168",

            "RollingMean_24",
            "RollingMean_168",
            "RollingStd_24",

            "Lag_2",
            "Lag_3",
            "Lag_6",
            "Lag_12",
            "Lag_48",
            "Lag_72"

        ]


        validation_hours = days * 24

        validation_df = df.tail(
            validation_hours
        ).copy()


        X_validation = validation_df[
            features
        ]

        X_validation_scaled = X_scaler.transform(
            X_validation
        )

        X_sequences = []

        y_actual = []

        dates = []

        sequence_length = 48


        for i in range(
            sequence_length,
            len(validation_df)
        ):

            X_sequences.append(
                X_validation_scaled[
                    i-sequence_length:i
                ]
            )

            y_actual.append(
                validation_df[
                    "PJME_MW"
                ].iloc[i]
            )

            dates.append(
                validation_df[
                    "Datetime"
                ].iloc[i]
            )


        X_sequences = np.array(
            X_sequences
        )

        predictions = model.predict(
            X_sequences,
            verbose=0
        )

        predictions = predictions[:, 0]

        predictions_original = y_scaler.inverse_transform(
            predictions.reshape(-1, 1)
        ).flatten()

        actual_array = np.array(
            y_actual
        )

        predicted_array = np.array(
            predictions_original
        )


        mae = mean_absolute_error(
            actual_array,
            predicted_array
        )

        rmse = np.sqrt(
            mean_squared_error(
                actual_array,
                predicted_array
            )
        )

        mape = np.mean(
            np.abs(
                (
                    actual_array -
                    predicted_array
                )
                /
                actual_array
            )
        ) * 100

        actual_values = [
            round(float(x), 2)
            for x in actual_array
        ]

        predicted_values = [
            round(float(x), 2)
            for x in predicted_array
        ]

        validation_dates = [

            x.strftime(
                "%Y-%m-%d %H:%M"
            )

            for x in dates
        ]


        mae = round(
            float(mae),
            2
        )

        rmse = round(
            float(rmse),
            2
        )

        mape = round(
            float(mape),
            2
        )


    return render_template(

        "validation.html",

        days=days,

        actual_values=actual_values,

        predicted_values=predicted_values,

        validation_dates=validation_dates,

        mae=mae,

        rmse=rmse,

        mape=mape

    )

if __name__ == "__main__":
    app.run(debug=True)