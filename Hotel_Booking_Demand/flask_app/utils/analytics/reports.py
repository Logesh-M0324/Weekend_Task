import pandas as pd

df = pd.read_csv("../data/processed/final_hotel_bookings.csv")


def get_executive_summary():

    return {

        "total_bookings": len(df),

        "total_cancellations": int(df["is_canceled"].sum()),

        "cancellation_rate": round(
            df["is_canceled"].mean() * 100,
            2
        ),

        "average_adr": round(
            df["average_daily_rate"].mean(),
            2
        ),

        "average_stay": round(
            df["total_stay_duration"].mean(),
            2
        )

    }


def get_booking_report():

    monthly = (

        df.groupby("arrival_date_month")

        .size()

        .reset_index(name="Bookings")

    )

    return monthly


def get_revenue_report():

    revenue = (

        df.groupby("market_segment")["average_daily_rate"]

        .mean()

        .reset_index()

    )

    revenue.columns = [

        "Market Segment",

        "Average ADR"

    ]

    return revenue


def get_customer_report():

    customer = (

        df.groupby("customer_type")

        .size()

        .reset_index(name="Customers")

    )

    return customer


def get_cancellation_report():

    cancellation = (

        df.groupby("deposit_type")["is_canceled"]

        .mean()

        .reset_index()

    )

    cancellation["Cancellation Rate"] = (

        cancellation["is_canceled"] * 100

    ).round(2)

    return cancellation[
        ["deposit_type", "Cancellation Rate"]
    ]


def get_statistical_report():

    normality = pd.read_csv(
        "../data/statistics/normality_summary.csv"
    )

    vif = pd.read_csv(
        "../data/statistics/vif_results.csv"
    )

    return {

        "normality": normality,

        "vif": vif

    }