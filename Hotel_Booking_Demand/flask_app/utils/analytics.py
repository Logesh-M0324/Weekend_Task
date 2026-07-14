from utils.loader import load_data
import pandas as pd

df = load_data()

# This function returns the important datasets data to showcase in the Home KPI card 

def get_dashboard_kpis():

    total_bookings = len(df)

    cancellation_rate = round(

        df["is_canceled"].mean() * 100,

        2

    )

    average_adr = round(

        df["average_daily_rate"].mean(),

        2

    )

    average_stay = round(

        df["total_stay_duration"].mean(),

        2

    )

    return {

        "total_bookings": total_bookings,

        "cancellation_rate": cancellation_rate,

        "average_adr": average_adr,

        "average_stay": average_stay

    }

# Get the Monthly_booking

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

    monthly = monthly.sort_values("arrival_date_month")

    return monthly


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