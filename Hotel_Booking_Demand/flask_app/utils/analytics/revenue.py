from utils.loader import load_data
import pandas as pd

df = load_data()


def get_revenue_kpis():

    total_revenue = (
        df["average_daily_rate"] *
        df["total_stay_duration"]
    ).sum()

    return {

        "average_adr": round(
            df["average_daily_rate"].mean(),
            2
        ),

        "maximum_adr": round(
            df["average_daily_rate"].max(),
            2
        ),

        "minimum_adr": round(
            df["average_daily_rate"].min(),
            2
        ),

        "total_revenue": round(
            total_revenue,
            2
        )

    }


def get_monthly_adr():

    month_order = [

        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"

    ]

    monthly = (

        df.groupby("arrival_date_month")[
            "average_daily_rate"
        ]

        .mean()

        .reset_index()

    )

    monthly["arrival_date_month"] = pd.Categorical(

        monthly["arrival_date_month"],

        categories=month_order,

        ordered=True

    )

    monthly = monthly.sort_values(
        "arrival_date_month"
    )

    return monthly


def get_hotel_revenue():

    revenue = (

        df.groupby("hotel")

        .apply(

            lambda x: (

                x["average_daily_rate"] *

                x["total_stay_duration"]

            ).sum()

        )

        .reset_index(
            name="revenue"
        )

    )

    return revenue


def get_market_segment_adr():

    segment = (

        df.groupby("market_segment")[

            "average_daily_rate"

        ]

        .mean()

        .reset_index()

    )

    return segment


def get_weekend_weekday_adr():

    weekday = (

        df["stays_in_week_nights"] *

        df["average_daily_rate"]

    ).sum()

    weekend = (

        df["stays_in_weekend_nights"] *

        df["average_daily_rate"]

    ).sum()

    return {

        "Weekday": round(weekday, 2),

        "Weekend": round(weekend, 2)

    }


def get_customer_type_adr():

    customer = (

        df.groupby("customer_type")[

            "average_daily_rate"

        ]

        .mean()

        .reset_index()

    )

    return customer