import pandas as pd

# Load the cleaned hotel booking dataset that will be used
# to generate reports and executive summaries.
df = pd.read_csv("../data/processed/final_hotel_bookings.csv")


# ---------------------------------------------------------
# Executive Summary Report
# ---------------------------------------------------------
def get_executive_summary():

    # Calculate the high-level business KPIs required
    # for the executive summary section of the report.
    return {

        # Total number of hotel bookings.
        "total_bookings": len(df),

        # Total number of cancelled bookings.
        "total_cancellations": int(df["is_canceled"].sum()),

        # Overall cancellation percentage.
        "cancellation_rate": round(
            df["is_canceled"].mean() * 100,
            2
        ),

        # Average Daily Rate (ADR) across all bookings.
        "average_adr": round(
            df["average_daily_rate"].mean(),
            2
        ),

        # Average duration of customer stay.
        "average_stay": round(
            df["total_stay_duration"].mean(),
            2
        )

    }


# ---------------------------------------------------------
# Booking Report
# ---------------------------------------------------------
def get_booking_report():

    # Calculate the number of bookings made in each
    # arrival month.
    monthly = (

        df.groupby("arrival_date_month")

        .size()

        .reset_index(name="Bookings")

    )

    return monthly


# ---------------------------------------------------------
# Revenue Report
# ---------------------------------------------------------
def get_revenue_report():

    # Calculate the average Daily Rate (ADR)
    # for each market segment.
    revenue = (

        df.groupby("market_segment")["average_daily_rate"]

        .mean()

        .reset_index()

    )

    # Rename columns for better readability
    # in reports and exported tables.
    revenue.columns = [

        "Market Segment",

        "Average ADR"

    ]

    return revenue


# ---------------------------------------------------------
# Customer Report
# ---------------------------------------------------------
def get_customer_report():

    # Count the number of customers
    # belonging to each customer type.
    customer = (

        df.groupby("customer_type")

        .size()

        .reset_index(name="Customers")

    )

    return customer


# ---------------------------------------------------------
# Cancellation Report
# ---------------------------------------------------------
def get_cancellation_report():

    # Calculate the cancellation percentage
    # for each deposit type.
    cancellation = (

        df.groupby("deposit_type")["is_canceled"]

        .mean()

        .reset_index()

    )

    # Convert cancellation probability into
    # percentage format.
    cancellation["Cancellation Rate"] = (

        cancellation["is_canceled"] * 100

    ).round(2)

    # Return only the required columns
    # for report generation.
    return cancellation[
        ["deposit_type", "Cancellation Rate"]
    ]


# ---------------------------------------------------------
# Statistical Analysis Report
# ---------------------------------------------------------
def get_statistical_report():

    # Load the normality test summary
    # generated during statistical analysis.
    normality = pd.read_csv(
        "../data/statistics/normality_summary.csv"
    )

    # Load the Variance Inflation Factor (VIF)
    # results used for multicollinearity analysis.
    vif = pd.read_csv(
        "../data/statistics/vif_results.csv"
    )

    # Return all statistical analysis outputs
    # as a dictionary for report generation.
    return {

        "normality": normality,

        "vif": vif

    }