from utils.loader import load_data
import pandas as pd

# Load the cleaned hotel booking dataset once when the module is imported.
# This DataFrame will be shared across all functions in this file.
df = load_data()


# ---------------------------------------------------------
# Monthly Booking Trend
# ---------------------------------------------------------
def get_monthly_bookings():

    # Group the dataset by arrival month and count the
    # total number of bookings for each month.
    monthly = (

        df.groupby("arrival_date_month")

        .size()

        .reset_index(name="bookings")

    )

    # Define the chronological order of months because
    # groupby() returns months in alphabetical order.
    month_order = [

        "January", "February", "March", "April",

        "May", "June", "July", "August",

        "September", "October", "November", "December"

    ]

    # Convert the month column into a categorical datatype
    # so the months follow the correct calendar sequence.
    monthly["arrival_date_month"] = pd.Categorical(

        monthly["arrival_date_month"],

        categories=month_order,

        ordered=True

    )

    # Return the DataFrame sorted according to the
    # chronological month order.
    return monthly.sort_values("arrival_date_month")


# ---------------------------------------------------------
# Hotel Type Comparison
# ---------------------------------------------------------
def get_hotel_type_bookings():

    # Count the total number of bookings made for each
    # hotel category (City Hotel and Resort Hotel).
    return (

        df.groupby("hotel")

        .size()

        .reset_index(name="bookings")

    )


# ---------------------------------------------------------
# Seasonal Booking Analysis
# ---------------------------------------------------------
def get_season_bookings():

    # Group bookings by booking season and calculate
    # the total bookings for each season.
    season = (

        df.groupby("booking_season")

        .size()

        .reset_index(name="bookings")

    )

    return season


# ---------------------------------------------------------
# Lead Time Distribution
# ---------------------------------------------------------
def get_lead_time_distribution():

    # Return all lead time values as a Python list.
    # This data is primarily used for histogram charts
    # showing booking lead time distribution.
    return df["lead_time"].tolist()


# ---------------------------------------------------------
# Booking KPI Metrics
# ---------------------------------------------------------
def get_booking_kpis():

    # Identify the month having the highest number
    # of hotel bookings.
    peak_month = (

        df["arrival_date_month"]

        .value_counts()

        .idxmax()

    )

    # Determine which hotel type receives
    # the maximum number of bookings.
    preferred_hotel = (

        df["hotel"]

        .value_counts()

        .idxmax()

    )

    # Calculate the average booking lead time
    # and round the result to one decimal place.
    average_lead_time = round(

        df["lead_time"].mean(),

        1

    )

    # Calculate the average total stay duration
    # (weekend nights + weekday nights).
    average_stay = round(

        df["total_stay_duration"].mean(),

        1

    )

    # Return all booking KPIs as a dictionary
    # for displaying summary cards on the dashboard.
    return {

        "peak_month": peak_month,

        "preferred_hotel": preferred_hotel,

        "average_lead_time": average_lead_time,

        "average_stay": average_stay

    }