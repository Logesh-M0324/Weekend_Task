from utils.loader import load_data
import pandas as pd

# Load the cleaned hotel booking dataset once when the module is imported.
# This DataFrame is shared across all revenue analytics functions.
df = load_data()


# ---------------------------------------------------------
# Revenue KPI Metrics
# ---------------------------------------------------------
def get_revenue_kpis():

    # Calculate the estimated total revenue by multiplying
    # Average Daily Rate (ADR) with total stay duration.
    total_revenue = (
        df["average_daily_rate"] *
        df["total_stay_duration"]
    ).sum()

    # Return the primary revenue KPIs used
    # in the Revenue Analytics dashboard.
    return {

        # Calculate the average ADR across all bookings.
        "average_adr": round(
            df["average_daily_rate"].mean(),
            2
        ),

        # Find the highest recorded ADR.
        "maximum_adr": round(
            df["average_daily_rate"].max(),
            2
        ),

        # Find the lowest recorded ADR.
        "minimum_adr": round(
            df["average_daily_rate"].min(),
            2
        ),

        # Calculate the estimated total revenue generated
        # from all hotel bookings.
        "total_revenue": round(
            total_revenue,
            2
        )

    }


# ---------------------------------------------------------
# Monthly Average ADR
# ---------------------------------------------------------
def get_monthly_adr():

    # Define the chronological order of months
    # for proper chart visualization.
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

    # Calculate the average ADR for each arrival month.
    monthly = (

        df.groupby("arrival_date_month")[
            "average_daily_rate"
        ]

        .mean()

        .reset_index()

    )

    # Convert month names into an ordered categorical
    # variable for chronological sorting.
    monthly["arrival_date_month"] = pd.Categorical(

        monthly["arrival_date_month"],

        categories=month_order,

        ordered=True

    )

    # Sort the DataFrame based on the month order.
    monthly = monthly.sort_values(
        "arrival_date_month"
    )

    return monthly


# ---------------------------------------------------------
# Revenue by Hotel Type
# ---------------------------------------------------------
def get_hotel_revenue():

    # Calculate total estimated revenue generated
    # by each hotel category.
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


# ---------------------------------------------------------
# Average ADR by Market Segment
# ---------------------------------------------------------
def get_market_segment_adr():

    # Calculate the average ADR generated
    # by each market segment.
    segment = (

        df.groupby("market_segment")[

            "average_daily_rate"

        ]

        .mean()

        .reset_index()

    )

    return segment


# ---------------------------------------------------------
# Weekend vs Weekday Revenue
# ---------------------------------------------------------
def get_weekend_weekday_adr():

    # Calculate total weekday revenue using
    # weekday stays multiplied by ADR.
    weekday = (

        df["stays_in_week_nights"] *

        df["average_daily_rate"]

    ).sum()

    # Calculate total weekend revenue using
    # weekend stays multiplied by ADR.
    weekend = (

        df["stays_in_weekend_nights"] *

        df["average_daily_rate"]

    ).sum()

    # Return the estimated revenue generated
    # during weekdays and weekends.
    return {

        "Weekday": round(weekday, 2),

        "Weekend": round(weekend, 2)

    }


# ---------------------------------------------------------
# Average ADR by Customer Type
# ---------------------------------------------------------
def get_customer_type_adr():

    # Calculate the average ADR for each
    # customer type category.
    customer = (

        df.groupby("customer_type")[

            "average_daily_rate"

        ]

        .mean()

        .reset_index()

    )

    return customer