from utils.loader import load_data

df = load_data()


def get_dashboard_kpis():

    return {

        "total_bookings": len(df),

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

def get_monthly_booking_trend():

    monthly = (

        df.groupby("arrival_date_month")

        .size()

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

    monthly.columns = [

        "Month",

        "Bookings"

    ]

    return monthly


def get_booking_status():

    status = (

        df["is_canceled"]

        .value_counts()

        .reset_index()

    )

    status.columns = [

        "Status",

        "Count"

    ]

    status["Status"] = status["Status"].replace(

        {

            0: "Completed",

            1: "Cancelled"

        }

    )

    return status

def get_executive_cards():

    total_countries = df["country"].nunique()

    hotel_types = df["hotel"].nunique()

    average_lead_time = round(
        df["lead_time"].mean(),
        1
    )

    repeat_guest_rate = round(
        (df["is_repeated_guest"].mean() * 100),
        2
    )

    return {

        "total_countries": total_countries,

        "hotel_types": hotel_types,

        "average_lead_time": average_lead_time,

        "repeat_guest_rate": repeat_guest_rate

    }