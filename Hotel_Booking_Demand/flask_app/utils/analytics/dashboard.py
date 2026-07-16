from utils.loader import load_data

# Load the cleaned hotel booking dataset once when the module is imported.
# This DataFrame is shared across all dashboard analytics functions.
df = load_data()


# ---------------------------------------------------------
# Dashboard KPI Metrics
# ---------------------------------------------------------
def get_dashboard_kpis():

    # Calculate the primary KPI metrics displayed
    # on the dashboard overview cards.
    return {

        # Total number of hotel bookings.
        "total_bookings": len(df),

        # Calculate the overall booking cancellation
        # percentage and round it to two decimal places.
        "cancellation_rate": round(
            df["is_canceled"].mean() * 100,
            2
        ),

        # Calculate the average daily room rate (ADR)
        # across all hotel bookings.
        "average_adr": round(
            df["average_daily_rate"].mean(),
            2
        ),

        # Calculate the average total stay duration
        # (weekday nights + weekend nights).
        "average_stay": round(
            df["total_stay_duration"].mean(),
            2
        )

    }


# ---------------------------------------------------------
# Monthly Booking Trend
# ---------------------------------------------------------
def get_monthly_booking_trend():

    # Group bookings by arrival month and count
    # the number of bookings in each month.
    monthly = (

        df.groupby("arrival_date_month")

        .size()

        # Reorder the months into chronological order
        # and fill missing months with zero bookings.
        .reindex(

            [

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

            ],

            fill_value=0

        )

        .reset_index()

    )

    # Rename the DataFrame columns to provide
    # meaningful labels for charts.
    monthly.columns = [

        "Month",

        "Bookings"

    ]

    return monthly


# ---------------------------------------------------------
# Booking Status Distribution
# ---------------------------------------------------------
def get_booking_status():

    # Count completed and cancelled bookings
    # and convert the result into a DataFrame.
    status = (

        df["is_canceled"]

        .value_counts()

        .reset_index()

    )

    # Rename the columns for better readability
    # in charts and dashboard components.
    status.columns = [

        "Status",

        "Count"

    ]

    # Replace numeric status values with descriptive
    # booking status labels.
    status["Status"] = status["Status"].replace(

        {

            0: "Completed",

            1: "Cancelled"

        }

    )

    return status


# ---------------------------------------------------------
# Executive Dashboard Cards
# ---------------------------------------------------------
def get_executive_cards():

    # Calculate the number of unique customer countries.
    total_countries = df["country"].nunique()

    # Calculate the number of hotel categories
    # available in the dataset.
    hotel_types = df["hotel"].nunique()

    # Compute the average booking lead time
    # before customer arrival.
    average_lead_time = round(
        df["lead_time"].mean(),
        1
    )

    # Calculate the percentage of repeat guests
    # across all hotel bookings.
    repeat_guest_rate = round(
        (df["is_repeated_guest"].mean() * 100),
        2
    )

    # Return executive-level summary metrics
    # for the dashboard overview section.
    return {

        "total_countries": total_countries,

        "hotel_types": hotel_types,

        "average_lead_time": average_lead_time,

        "repeat_guest_rate": repeat_guest_rate

    }