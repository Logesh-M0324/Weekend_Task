from utils.loader import load_data
import pandas as pd

df = load_data()


def get_monthly_bookings():

    monthly = (

        df.groupby("arrival_date_month")

        .size()

        .reset_index(name="bookings")

    )

    month_order = [

        "January","February","March","April",

        "May","June","July","August",

        "September","October","November","December"

    ]

    monthly["arrival_date_month"] = pd.Categorical(

        monthly["arrival_date_month"],

        categories=month_order,

        ordered=True

    )

    return monthly.sort_values("arrival_date_month")

# Hotel Type comparison

def get_hotel_type_bookings():

    return (

        df.groupby("hotel")

        .size()

        .reset_index(name="bookings")

    )

# Seasonal Bookings

def get_season_bookings():

    season = (

        df.groupby("booking_season")

        .size()

        .reset_index(name="bookings")

    )

    return season


# Lead Time Distribution

def get_lead_time_distribution():

    return df["lead_time"].tolist()


def get_booking_kpis():

    peak_month = (

        df["arrival_date_month"]

        .value_counts()

        .idxmax()

    )

    preferred_hotel = (

        df["hotel"]

        .value_counts()

        .idxmax()

    )

    average_lead_time = round(

        df["lead_time"].mean(),

        1

    )

    average_stay = round(

        df["total_stay_duration"].mean(),

        1

    )

    return {

        "peak_month": peak_month,

        "preferred_hotel": preferred_hotel,

        "average_lead_time": average_lead_time,

        "average_stay": average_stay

    }