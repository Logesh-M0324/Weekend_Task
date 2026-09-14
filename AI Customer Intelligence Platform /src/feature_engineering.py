import pandas as pd
import numpy as np


def create_features(df):
    df = df.copy()

    # -----------------------------
    # Basic data type correction
    # -----------------------------
    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    df["TotalCharges"] = df["TotalCharges"].fillna(0)

    # -----------------------------
    # Tenure features
    # -----------------------------
    df["TenureGroup"] = pd.cut(
        df["tenure"],
        bins=[-1, 12, 24, 48, 72],
        labels=[
            "New",
            "Early",
            "Mid",
            "Long-term"
        ]
    )

    df["IsNewCustomer"] = (
        df["tenure"] <= 12
    ).astype(int)

    df["IsLongTermCustomer"] = (
        df["tenure"] >= 48
    ).astype(int)

    # -----------------------------
    # Service features
    # -----------------------------
    service_columns = [
        "PhoneService",
        "MultipleLines",
        "InternetService",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies"
    ]

    df["NumberOfServices"] = 0

    for column in service_columns:
        df["NumberOfServices"] += (
            ~df[column].isin(
                ["No", "No internet service"]
            )
        ).astype(int)

    optional_service_columns = [
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies"
    ]

    df["OptionalServiceCount"] = 0

    for column in optional_service_columns:
        df["OptionalServiceCount"] += (
            df[column] == "Yes"
        ).astype(int)

    df["HasInternetService"] = (
        df["InternetService"] != "No"
    ).astype(int)

    df["IsFiberCustomer"] = (
        df["InternetService"] == "Fiber optic"
    ).astype(int)

    # -----------------------------
    # Charge features
    # -----------------------------
    monthly_q1 = df["MonthlyCharges"].quantile(0.25)
    monthly_q2 = df["MonthlyCharges"].quantile(0.50)
    monthly_q3 = df["MonthlyCharges"].quantile(0.75)

    df["MonthlyChargeGroup"] = pd.cut(
        df["MonthlyCharges"],
        bins=[
            -np.inf,
            monthly_q1,
            monthly_q2,
            monthly_q3,
            np.inf
        ],
        labels=[
            "Low",
            "Medium",
            "High",
            "Very High"
        ]
    )

    total_q1 = df["TotalCharges"].quantile(0.25)
    total_q2 = df["TotalCharges"].quantile(0.50)
    total_q3 = df["TotalCharges"].quantile(0.75)

    df["TotalChargeGroup"] = pd.cut(
        df["TotalCharges"],
        bins=[
            -np.inf,
            total_q1,
            total_q2,
            total_q3,
            np.inf
        ],
        labels=[
            "Low",
            "Medium",
            "High",
            "Very High"
        ]
    )

    df["ChargePerTenure"] = np.where(
        df["tenure"] > 0,
        df["TotalCharges"] / df["tenure"],
        df["MonthlyCharges"]
    )

    high_value_threshold = (
        df["MonthlyCharges"].quantile(0.75)
    )

    df["HighValueCustomer"] = (
        df["MonthlyCharges"] >= high_value_threshold
    ).astype(int)

    # -----------------------------
    # Contract/payment features
    # -----------------------------
    df["MonthToMonthContract"] = (
        df["Contract"] == "Month-to-month"
    ).astype(int)

    df["ElectronicCheck"] = (
        df["PaymentMethod"] == "Electronic check"
    ).astype(int)

    # -----------------------------
    # Service risk features
    # -----------------------------
    df["NoTechSupport"] = (
        df["TechSupport"] == "No"
    ).astype(int)

    df["NoOnlineSecurity"] = (
        df["OnlineSecurity"] == "No"
    ).astype(int)

    df["ServiceRiskIndicator"] = (
        (
            (df["MonthToMonthContract"] == 1)
            & (df["NoOnlineSecurity"] == 1)
            & (df["NoTechSupport"] == 1)
        )
    ).astype(int)

    df["HighRiskCustomer"] = (
        (
            (df["MonthToMonthContract"] == 1)
            & (df["IsNewCustomer"] == 1)
            & (df["HighValueCustomer"] == 1)
        )
    ).astype(int)

    return df